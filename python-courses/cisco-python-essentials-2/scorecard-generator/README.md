# Cricket T20 Scorecard Generator

A console-based Python application for creating and analyzing detailed cricket T20 scorecards. This tool is ideal for learning, coaching, recording matches, or just for fun!

---

## Features

- **Interactive Team Setup**
  - Enter both teams (11 players each, with shirt numbers and names).
  - Support for reusable teams with the `teams/` folder (`_XI.csv` files).
  - Load and save teams to CSV for quick setup.

- **Ball-by-Ball Input**
  - Select opening batters and bowlers from ordered team lists.
  - Input every ball of the innings: runs, wickets, extras (wides, no balls, byes, leg byes), with error checking and friendly prompts.
  - T20-specific rules: 2 overs per match (for demo/learning, can adjust), 1 over max per bowler (for demo/learning).
  - Handles striker/non-striker swaps correctly—including after overs and for odd runs/extras.

- **Wicket Handling**
  - On each wicket, displays current score (`runs-wickets`), batter summary, and prompts for the next batter from only the eligible remaining players.
  - Fixes and prevents non-striker reappearing as "yet to bat" after a wicket.

- **Scorecard Output**
  - Professional-style batting and bowling scorecards:
    - **Batting:** Player Name, Dismissal (cricket notation), Runs, Balls, 4s, 6s, Strike Rate
    - **Bowling:** Bowler, Overs, Maidens, Runs, Wkts, Econ, Dots, 4s, 6s, Wides, Noballs
    - Extras, totals, "Did not bat", and fall of wickets
  - Output formatting is robust and readable in the console.

- **Robust Error Handling**
  - Friendly prompts and `"you can't do that try again."` messages for invalid or inconsistent inputs.
  - Prevents picking the same batter twice, ensures team order is preserved, and handles edge cases like all out or innings ended early.

---

## Usage

1. Run the program:
   ```bash
   python scorecard_generator.py
   ```

2. Follow the prompts:
    - Enter team names and players (11 per team, or load from CSV files)
    - Choose openers and bowlers by order or shirt number
    - Enter the result of each ball (runs, wicket, extras, etc.)
    - On wickets, select the next batter from a filtered, eligible list
    - After the innings, view full batting and bowling scorecards

---

## File Structure

- [`scorecard_generator.py`](scorecard_generator.py) — main script for running the scorecard generator
- [`teams/`](teams/) — folder for reusable team/player data as `_XI.csv` files

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
