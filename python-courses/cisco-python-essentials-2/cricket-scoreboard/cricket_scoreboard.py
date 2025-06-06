import os

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
                lines[i] += "     "  # For non-digits (spaces)
    return lines

class Player:
    def __init__(self, name, runs=0):
        self.name = name
        self.runs = runs

    def __str__(self):
        return f"{self.name:<15} {self.runs:>3}"

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def total_runs(self):
        return sum(player.runs for player in self.players)

    def __str__(self):
        s = f"\n{self.name} Batting:\n"
        s += "-"*22 + "\n"
        for p in self.players:
            s += f"{p}\n"
        s += "-"*22 + "\n"
        s += f"Total: {self.total_runs()} runs\n"
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
                # Format: PlayerName,Runs
                if current_team:
                    parts = line.split(",")
                    if len(parts) == 2 and parts[1].isdigit():
                        current_team.add_player(Player(parts[0].strip(), int(parts[1].strip())))
    
    def display(self):
        for team in self.teams:
            print(team)
            total = team.total_runs()
            print("Score in ASCII art:")
            for line in ascii_number(total):
                print(line)
            print()

def main():
    print("ASCII Art Cricket Scoreboard")
    filename = input("Enter match score filename (e.g. match.txt): ").strip()
    scoreboard = Scoreboard()
    scoreboard.load_from_file(filename)
    scoreboard.display()

if __name__ == "__main__":
    main()
