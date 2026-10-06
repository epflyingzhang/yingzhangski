#!/usr/bin/env python3
import os
import sys
import json
import urllib.request
import urllib.parse
from datetime import datetime, timedelta, timezone

CALENDLY_TOKEN = os.environ.get("CALENDLY_TOKEN")

if not CALENDLY_TOKEN:
    print("[Error] CALENDLY_TOKEN environment variable is missing.")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {CALENDLY_TOKEN}",
    "Content-Type": "application/json"
}

def api_get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def get_zurich_date(iso_str):
    # Parse ISO string
    dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    # Approximate Zurich offset (CET/CEST) UTC+1 or UTC+2
    # Simple month check for CEST (April-October)
    offset = timedelta(hours=2) if (4 <= dt.month <= 10) else timedelta(hours=1)
    zurich_dt = dt.astimezone(timezone(offset))
    return zurich_dt

WEEKDAYS = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]

def main():
    print("Fetching user profile from Calendly API...")
    user_data = api_get("https://api.calendly.com/users/me")
    user_uri = user_data["resource"]["uri"]
    print(f"User URI: {user_uri}")

    print("Fetching event types...")
    event_types_url = f"https://api.calendly.com/event_types?user={urllib.parse.quote(user_uri)}"
    event_types_data = api_get(event_types_url)

    target_event_uri = None
    for et in event_types_data.get("collection", []):
        slug = et.get("slug", "")
        print(f"Found event type: {et.get('name')} (slug: {slug})")
        if slug == "private-lesson-half-day" or "private" in slug.lower():
            target_event_uri = et.get("uri")
            print(f"Selected target event type URI: {target_event_uri}")
            break

    if not target_event_uri and event_types_data.get("collection"):
        target_event_uri = event_types_data["collection"][0]["uri"]
        print(f"Fallback to first event type URI: {target_event_uri}")

    if not target_event_uri:
        print("[Error] No active event types found.")
        sys.exit(1)

    now = datetime.now(timezone.utc)
    start_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    end_time = (now + timedelta(days=45)).strftime("%Y-%m-%dT%H:%M:%SZ")

    avail_url = f"https://api.calendly.com/event_type_available_times?event_type={urllib.parse.quote(target_event_uri)}&start_time={start_time}&end_time={end_time}"
    print(f"Fetching availability from {start_time} to {end_time}...")
    avail_data = api_get(avail_url)

    collection = avail_data.get("collection", [])
    print(f"Total available slots returned: {len(collection)}")

    unique_dates = []
    seen_date_strings = set()

    for item in collection:
        if item.get("status") == "available":
            iso_start = item.get("start_time")
            dt = get_zurich_date(iso_start)
            date_key = dt.strftime("%Y-%m-%d")
            
            if date_key not in seen_date_strings:
                seen_date_strings.add(date_key)
                
                date_str = f"{dt.month}月{dt.day}日"
                weekday_str = WEEKDAYS[dt.weekday()]
                time_str = dt.strftime("%H:%M")
                
                unique_dates.append({
                    "date": date_str,
                    "weekday": weekday_str,
                    "time": time_str,
                    "iso": iso_start
                })

                if len(unique_dates) == 4:
                    break

    output = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "event_type": "private-lesson-half-day",
        "next_4_dates": unique_dates
    }

    os.makedirs("./assets", exist_ok=True)
    
    # Save as JSON
    json_file = "./assets/availability.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    # Save as JS script object for CORS-free local and remote loading
    js_file = "./assets/availability.js"
    with open(js_file, "w", encoding="utf-8") as f:
        f.write(f"window.CALENDLY_AVAILABILITY = {json.dumps(output, ensure_ascii=False, indent=2)};\n")

    print(f"Successfully saved {len(unique_dates)} dates to {json_file} and {js_file}")

if __name__ == "__main__":
    main()
