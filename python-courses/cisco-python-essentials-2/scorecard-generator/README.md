# Cricket T20 Scorecard Generator

A console-based Python application for creating and analyzing detailed cricket T20 scorecards. This tool is ideal for learning, coaching, recording matches, or just for fun!

---

## Features

- **Interactive Team Management (`teams_utils.py`):**
  - Create and edit reusable teams and player squads.
  - Enforce unique shirt numbers and valid player names.
  - Easily manage squads larger than 11 (for selection flexibility).
  - List, edit, and update teams from the console.
  - Select and save a starting XI for a match, assigning captain and wicket-keeper roles.
  - Stores teams and XIs in the `teams/` folder as CSV files for reuse.

- **Interactive Team Setup (`scorecard_generator.py`):**
  - Load playing XIs directly from CSV files created by `teams_utils.py`.
  - Enter both teams (11 players each, with shirt numbers and names).
  - [Optional] Enter teams manually if not using the team manager.

- **Ball-by-Ball Input**
  - Select opening batters and bowlers from ordered team lists.
  - Input every ball of the innings: runs, wickets, extras (wides, no balls, byes, leg byes), with error checking and friendly prompts.
  - T20-specific rules (demo version): 2 overs per match, 1 over max per bowler (adjustable).
  - Handles striker/non-striker swaps correctly—including after overs and for odd runs/extras.

- **Wicket Handling**
  - On each wicket, displays current score (`runs-wickets`), batter summary, and prompts for the next batter from only the eligible remaining players.
  - Prevents non-striker from appearing as "yet to bat" after a wicket.

- **Scorecard Output**
  - Professional-style batting and bowling scorecards:
    - **Batting:** Player Name, Dismissal (cricket notation), Runs, Balls, 4s, 6s, Strike Rate
    - **Bowling:** Bowler, Overs, Maidens, Runs, Wkts, Econ, Dots, 4s, 6s, Wides, Noballs
    - Extras, totals, "Did not bat", and fall of wickets
  - Output formatting is robust and readable in the console.

- **Robust Error Handling**
  - Friendly prompts and `"you can't do that try again."` messages for invalid or inconsistent inputs.
  - Prevents picking the same batter twice, ensures team order is preserved, and handles edge cases like all out or innings ended early.

- **Modular Design**
  - `scorecard_generator.py` – Main match/scorecard logic.
  - `teams_utils.py` – Team/squad management and XI selector utility (run directly for team management).
  - `teams/` – Folder for reusable team/squad/XI CSVs.

---

## Usage

### Team Management (Recommended)

1. Run the team manager to create/edit teams and pick your XI:
   ```bash
   python teams_utils.py
   ```
   - Create or edit teams and squads
   - Select a starting XI and assign captain/wicket-keeper
   - XIs saved as CSV in the `teams/` folder

### Scorecard Generator

2. Run the scorecard generator:
   ```bash
   python scorecard_generator.py
   ```
   - Load XIs from file or enter manually
   - Follow prompts for toss, openers, bowlers, and ball-by-ball input
   - See full batting and bowling scorecards after the innings

---

## File Structure

- [`scorecard_generator.py`](scorecard_generator.py) — main script for running the scorecard generator
- [`teams_utils.py`](teams_utils.py) — team/squad manager, XI selector utility
- [`teams/`](teams/) — folder for reusable team/squad/XI CSV files

---

## Example Output

```
Batting: Team A
Player Name         Dismissal                Runs Balls 4s  6s     SR
Alice Smith         c Jones b Patel             35    27  4   2  129.63
...
Extras                                         11
Total: 2.0 Ov (RR: 7.80) 156/6
Did not bat: Bob, Carol, Eve
Fall of wickets:
 1-22 (Patel, 0.3 ov), 2-45 (Jones, 1.1 ov), ...
...
Bowling: Team B
Bowler              Overs Maidens Runs Wkts  Econ Dots 4s 6s Wides Noballs
Kevin Patel         1.0      0    15   2   7.50    3   1  0     1      0
...
```

---

## Changelog / Recent Improvements

- Added `teams_utils.py` for robust team and squad management.
- Improved striker/non-striker swap logic at the end of overs.
- Fixed bug: non-striker never appears as eligible to bat after a wicket.
- Added clear messages for early innings or over endings (e.g., all out).
- Robust handling for team loading, input, and batting order management.
- Expanded prompts and error messages for better user experience.

---

## To Improve / TODO

- Add support for full 20-over innings and second innings with result calculation.
- Export scorecard to file (txt/CSV/JSON).
- Support for other formats (ODI, Test).
- More summary statistics and user guidance.
- Optional integration with external cricket data APIs.

---

*Part of the [Python Portfolio](https://github.com/mama-cailleach/python-portfolio/) — Cisco Python Essentials 2*
