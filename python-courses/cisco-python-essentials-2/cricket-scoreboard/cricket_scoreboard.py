import os
import time

NUMBER_ART = [
    [
        " ### ",
        "#   #",
        "#   #",
        "#   #",
        " ### "
    ],
    [
        "  #  ",
        " ##  ",
        "  #  ",
        "  #  ",
        " ### "
    ],
    [
        " ### ",
        "#   #",
        "   # ",
        "  #  ",
        "#####"
    ],
    [
        " ### ",
        "#   #",
        "  ## ",
        "#   #",
        " ### "
    ],
    [
        "#   #",
        "#   #",
        "#####",
        "    #",
        "    #"
    ],
    [
        "#####",
        "#    ",
        "#### ",
        "    #",
        "#### "
    ],
    [
        " ### ",
        "#    ",
        "#### ",
        "#   #",
        " ### "
    ],
    [
        "#####",
        "    #",
        "   # ",
        "  #  ",
        "  #  "
    ],
    [
        " ### ",
        "#   #",
        " ### ",
        "#   #",
        " ### "
    ],
    [
        " ### ",
        "#   #",
        " ####",
        "    #",
        " ### "
    ],
]

def ascii_number(n):
    """Return list of strings, each line of ASCII art for the number n (string or int)."""
    n_str = str(n)
    lines = ['' for _ in range(5)]
    for digit in n_str:
        if digit.isdigit():
            art = NUMBER_ART[int(digit)]
            for i in range(5):
                lines[i] += art[i] + "  "
        else:
            for i in range(5):
                lines[i] += "     "
    return lines

def ascii_score(runs, wickets):
    """Return ascii art for runs-wickets (e.g., 187-5)"""
    runs_lines = ascii_number(runs)
    dash = ["  -  "]*5
    wickets_lines = ascii_number(wickets)
    return [
        runs_lines[i] + dash[i] + wickets_lines[i]
        for i in range(5)
    ]

class Player:
    def __init__(self, name, runs=0, wicket_taker=None):
        self.name = name
        self.runs = runs
        self.wicket_taker = wicket_taker  # None if not out

    def __str__(self):
        out_info = f"  ({self.wicket_taker})" if self.wicket_taker else ""
        return f"{self.name:<18} {self.runs:>3}{out_info}"

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def total_runs(self):
        return sum(player.runs for player in self.players)

    def total_wickets(self):
        return sum(1 for p in self.players if p.wicket_taker)

    def wicket_takers(self):
        wickets = {}
        for p in self.players:
            if p.wicket_taker:
                wickets[p.wicket_taker] = wickets.get(p.wicket_taker, 0) + 1
        return wickets

    def __str__(self):
        s = f"\n{'Player':<18} {'Runs':>3}  Out By\n"
        s += "-"*34 + "\n"
        for p in self.players:
            s += f"{p}\n"
        s += "-"*34 + "\n"
        s += f"Total: {self.total_runs()} runs, {self.total_wickets()} wickets\n"
        return s

class Scoreboard:
    def __init__(self):
        self.teams = []

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            print("Score file not found.")
            return
        with open(filename) as f:
            lines = f.readlines()
        current_team = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("Team:"):
                current_team = Team(line[5:].strip())
                self.teams.append(current_team)
            else:
                # Format: PlayerName,Runs,WicketTaker(optional)
                if current_team:
                    parts = [part.strip() for part in line.split(",")]
                    name = parts[0]
                    runs = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0
                    wicket_taker = parts[2] if len(parts) > 2 and parts[2] else None
                    current_team.add_player(Player(name, runs, wicket_taker))
    
    def display(self):
        for idx, team in enumerate(self.teams):
            innings = "1st" if idx == 0 else "2nd"
            print(f"\n{innings} Innings: {team.name} Batting\n{'='*40}")
            print(team)
            time.sleep(1)
            print("Score (Runs - Wickets):")
            for line in ascii_score(team.total_runs(), team.total_wickets()):
                print(line)
            print("\nWicket Takers:")
            for bowler, wickets in team.wicket_takers().items():
                print(f"  {bowler}: {wickets}")
            print("\n" + "="*40)
            time.sleep(2 if idx == 0 else 1)

    def announce_winner(self):
        if len(self.teams) < 2:
            print("Not enough teams loaded.")
            return
        t1, t2 = self.teams[0], self.teams[1]
        runs1, wickets1 = t1.total_runs(), t1.total_wickets()
        runs2, wickets2 = t2.total_runs(), t2.total_wickets()
        print("\nFinal Result:")
        if runs2 > runs1:
            wickets_left = len(t2.players) - wickets2
            print(f"Winner: {t2.name} by {wickets_left} wickets!")
        elif runs1 > runs2:
            print(f"Winner: {t1.name} by {runs1 - runs2} runs!")
        else:
            print("Match Tied!")

def main():
    print("ASCII Art Cricket Scoreboard")
    filename = input("Enter match score filename (e.g. match.txt): ").strip()
    scoreboard = Scoreboard()
    scoreboard.load_from_file(filename)
    scoreboard.display()
    scoreboard.announce_winner()

if __name__ == "__main__":
    main()
