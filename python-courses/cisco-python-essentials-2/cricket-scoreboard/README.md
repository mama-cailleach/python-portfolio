# ASCII Art Cricket Scoreboard

A command-line Python program that displays a cricket match scoreboard with ASCII art numbers for both runs and wickets. Designed for easy parsing of real or custom cricket match data.

## Features

- Loads team and player scores (with wicket-takers) from a file (see `match.txt` example below)
- Displays each team's innings with clear separation ("1st Innings", "2nd Innings")
- Shows runs-wickets (e.g., 187-5) as large ASCII art digits
- Lists the wicket-takers and their wicket counts for each innings
- Short pauses between innings and before displaying totals for a more dramatic, readable output
- Declares the winner and margin (by runs or wickets) at the end
- Modular, object-oriented code (Player, Team, Scoreboard classes)

## Concepts Demonstrated

- String formatting and manipulation
- File input/output
- Classes (Player, Team, Scoreboard)
- ASCII art and custom number rendering
- Modular, extensible design
- Simple use of `time.sleep()` for user experience

## How to Run

```bash
python ascii_cricket_scoreboard.py
```

You will be prompted for a filename (e.g., `match.txt`).  
**Simply place your `match.txt` file in the same folder as the script, or enter a path to it when prompted.**

## Example Score File Format (`match.txt`)

Each team’s section starts with `Team: TeamName`, followed by each player’s line:

```
PlayerName,Runs,WicketTaker
```
- **WicketTaker** can be left blank or omitted for not-out batters.

**Example:**
```
Team: New Zealand Women
Suzie Bates,32,Nonkululeko Mlaba
Georgia Plimmer,9,Ayabonga Khaka
Amelia Kerr,43,Nonkululeko Mlaba
Sophie Devine,6,Nadine de Klerk
Brooke Halliday,38,Chloe Tryon
Maddy Green,12,
Isabella Gaze,3,
Extras,15,

Team: South Africa Women
Laura Wolvaardt,33,Amelia Kerr
Tazmin Brits,17,Fran Jonas
Anneke Bosch,9,Amelia Kerr
Marizanne Kapp,8,Eden Carson
Nadine de Klerk,6,Rosemary Mair
Chloe Tryon,14,Rosemary Mair
Sune Luus,8,Brooke Halliday
Annerie Dercksen,10,Amelia Kerr
Sinalo Jafta,6,Rosemary Mair
Nonkululeko Mlaba,4,
Ayabonga Khaka,4,
Extras,7
```

## A ready-to-use `match.txt` is included

For your convenience, a `match.txt` example is provided as the above.  
**The Women's T20 2024 World Cup Final between New Zealand and South Africa**.

## Possible Extensions

- Highlight highest scorer or key performers in ASCII art
- Add wickets, overs, and extras in detail
- Allow live input and updates from the CLI
- Save new scores or results from the program

---
