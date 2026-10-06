# Instructions for the Coding Agent (Template)

Welcome! This document outlines the guidelines, rules, and technical standards you must follow when implementing features or modifying this codebase. 

---

## 1. Project Context & Stack
<!-- Provide a high-level overview of what this project does and the technology stack it uses. -->
* **Core Technology:** [e.g., HTML/CSS/JS, React, Python, Node.js]
* **Design/Styling System:** [e.g., Vanilla CSS, Tailwind, Styled Components]
* **Primary Objective:** [e.g., Build features specified in prd.md, increase conversion, fix bugs]

---

## 2. Core Repository Structure
<!-- Map out the primary files and directories so the agent knows where to read and write code. -->
* `[path/to/main_file]` - [Description of what this file does]
* `[path/to/design_document]` - [Description (e.g. prd.md)]
* `[path/to/assets/]` - [Description of asset directory]

---

## 3. Coding Guidelines & Tech Standards
<!-- Define formatting, structure, and aesthetic rules. -->

### 3.1 Styling & UI/UX Standards
* **Design Tokens:** [e.g., Use CSS variables defined in :root; do not hardcode colors]
* **Theme:** [e.g., Dark-themed alpine winter palette, glassmorphism overlays]
* **Transitions:** [e.g., All interactive elements must have transition: all 0.3s ease]
* **Responsiveness:** [e.g., Support mobile devices down to 320px width up to 1440px desktop screens]

### 3.2 HTML & SEO Standards
* **Semantics:** [e.g., Use HTML5 structural tags (header, main, section, footer)]
* **Accessibility:** [e.g., Ensure all interactive controls have unique IDs and ARIA labels]
* **Tracking:** [e.g., Never modify or delete existing analytics/tag manager scripts unless asked]

---

## 4. Step-by-Step Workflow

When executing any coding task, follow these steps:

### Step 1: Analyze Requirements
* Open and read `prd.md` to locate the section or feature you are modifying/implementing.
* Trace any dependencies or linked documents.

### Step 2: Plan the Changes
* Identify which files need to be modified or created.
* Draft an implementation strategy.

### Step 3: Implement & Edit
* Write clean, documented code complying with the guidelines in Section 3.
* Ensure all links have correct targets and security attributes (e.g., `target="_blank" rel="noopener"` for external tabs).

### Step 4: Verification & Compliance
* Validate the code runs without warnings or console errors.
* Verify responsiveness and alignment across viewport sizes.

---

## 5. Explicit Rules (Do's & Don'ts)

### ✅ Do:
* [e.g., Keep comments and docstrings intact unless updating them is part of the feature.]
* [e.g., Use relative links for internal assets and absolute links for external URLs.]

### ❌ Don't:
* [e.g., Do not install new dependencies (via npm/pip) without prior user approval.]
* [e.g., Do not add placeholder code or "TODO" comments in production files.]
