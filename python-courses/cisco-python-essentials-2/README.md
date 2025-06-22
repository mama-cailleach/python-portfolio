# Cisco Python Essentials 2 – Project Portfolio

This folder contains a collection of intermediate Python projects created after completing the Cisco Python Essentials 2 course. These projects build on foundational skills and introduce more advanced programming concepts and practical applications.

---

## About the Course

**Cisco Python Essentials 2** is an intermediate programming course by Cisco Networking Academy.  
It expands on basic Python knowledge, covering advanced data structures, OOP, file handling, modules, and practical problem-solving.  
Learn more about the course [here](https://www.netacad.com/courses/python-essentials-2).

### Skills Gained

- Object-Oriented Programming (OOP)
- Advanced Data Structures (lists, dicts, sets, tuples)
- File Handling (CSV, text, JSON)
- Modular Programming & Packages
- Exception Handling
- Working with Dates & Times
- CLI Apps & User Interaction
- Real-world Problem Solving

---
## Major Project: Scorecard Generator (In Development)

### Cricket T20 Scorecard Generator
A complete, modular Python application for creating and analyzing detailed cricket T20 scorecards.
**Status:** _Complete for portfolio purposes, future development continuing in a dedicated repository_

- **Modular, professional Python codebase** split into dedicated modules:
  - Data models, team management, input handling, game logic, scorecard formatting
  - Package structure with proper setup.py configuration
- **Interactive team/squad management:**
  - Create/edit teams and squads, enforce unique shirt numbers
  - Assign captain and wicketkeeper roles, saved in CSV format
  - Select and save starting XIs for matches
- **Comprehensive match play experience:**
  - Ball-by-ball T20 input with robust validation
  - All cricket rules enforced (overs, wickets, bowler rest, etc.)
  - Professional scorecards with proper cricket notation
  - Basic match simulation functionality for testing
- **Demonstrates developer growth:**
  - Both legacy monolithic script and modern refactored version included
  - Shows evolution of coding practices and organization
  - Includes proper documentation and usage examples

See [`python-courses/cisco-python-essentials-2/scorecard-generator/`](./python-courses/cisco-python-essentials-2/scorecard-generator/) for full code and detailed README

---

## Other Projects

### Calendar Utility
A tool to display and manipulate calendars, check leap years, and calculate date differences. Demonstrates use of Python's `datetime` and `calendar` modules.

### Cricket Scoreboard
A console-based ASCII art cricket scoreboard. Loads match data, displays scores and wickets in large ASCII numbers, and summarizes innings.

### Cricket Stats CLI
A command-line application for analyzing and displaying cricket statistics from match data. Calculates batting, bowling, and partnership stats.

### Guess the Card
A simple CLI card-guessing game. Randomly draws a card and prompts the user to guess its value and suit.

### Train Simulator
Simulates a simple train station and journey manager. Practice with classes, lists, and file input/output.

### Study Folder
A collection of smaller scripts, notes, or experiments created during the course for practice and study.

---

## How to Run

Navigate into any project folder and run its main Python file.  
Example:
```bash
cd cricket-scoreboard
python ascii_cricket_scoreboard.py
```
Or open and run in [GitHub Codespaces](https://github.com/features/codespaces) for a cloud-based Python environment.

Each project folder includes its own `README.md` or docstring with more details and extension ideas.

---

## Certification

I have completed the Cisco Python Essentials 2 course and earned the official digital badge on May 30, 2025.  
You can verify my achievement on [Credly](https://www.credly.com/badges/41bc4436-10a3-4cce-bab2-ad37c1ee04db).
