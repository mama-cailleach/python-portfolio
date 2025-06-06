# Cricket T20 Scorecard Generator

A console-based Python application for creating and analyzing detailed cricket T20 scorecards. This tool is ideal for learning, coaching, recording matches, or just for fun!

## Features

- **Interactive Team Setup**
  - Enter both teams (11 players each, with shirt numbers and names).
  - [Optional] Extend with the `teams/` folder for reusable team/player info.

- **Ball-by-Ball Input**
  - Select opening batters and bowlers.
  - Input each ball of the innings (runs, wickets, extras, etc.) with error checking and prompts.
  - T20-specific rules: 20 overs maximum, 4 overs per bowler, one-over rest required between overs for bowlers.

- **Wicket Handling**
  - On each wicket, displays the current score (`runs-wickets`), batter summary, and prompts for the next batter from the remaining players.

- **Scorecard Output**
  - Professional batting and bowling scorecards:
    - Batting: No, Player Name, Dismissal, Runs, Balls, 4s, 6s, SR
    - Dismissals in cricket notation (e.g., `c Smith b Jones`, `lbw b Patel`, `run out(Clark)`, `not out`)
    - Extras and total
    - "Did not bat" section
    - Fall of wickets (runs, batter, bowler, over)
    - Bowling: Bowler, Overs, Maidens, Runs, Wkts, Econ, Dots, 4s, 6s, Wides, Noballs

- **Robust Error Handling**
  - Friendly prompts and `"you can't do that try again."` messages for invalid inputs.

## Usage

1. Run the program:
   ```bash
   python scorecard_generator.py
   ```
2. Follow the prompts:
    - Enter team names and players (11 per team)
    - Choose openers and bowlers, then enter each ball's result
    - On wickets, pick new batters as prompted
    - View the full batting and bowling scorecards after the innings

## File Structure

- [`scorecard_generator.py`](scorecard_generator.py) — main script for running the scorecard generator
- [`teams/`](teams/) — (optional) folder for future team/player data extensions

## Example Output

```
Batting: Team A
No  Player Name         Dismissal                Runs Balls 4s  6s     SR
7   Alice Smith         c Jones b Patel             35    27  4   2  129.63
...
    Extras                                         11
Total: 156 Ov (7.80) Runs/6
Did not bat: Bob, Carol, Eve
Fall of wickets:
 1-22 (Patel, 3.2 ov), 2-45 (Jones, 6.1 ov), ...
...
Bowling: Team B
Bowler              Overs Maidens Runs Wkts  Econ Dots 4s 6s Wides Noballs
Kevin Patel          4.0      0    31   2   7.75    8   3  1     2      0
...
```

## To Improve / TODO

- Add second innings and match result calculation
- Export scorecard to file (txt/CSV/JSON)
- Support for other formats (ODI, Test)
- More user guidance and summary stats
- Integrate with external cricket data APIs

---

*Part of the [Python Portfolio](https://github.com/mama-cailleach/python-portfolio/) — Cisco Python Essentials 2*
