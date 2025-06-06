import os

class Player:
    def __init__(self, name):
        self.name = name
        self.runs = 0
        self.wickets = 0

    def add_runs(self, runs):
        self.runs += runs

    def add_wicket(self):
        self.wickets += 1

    def __str__(self):
        return f"{self.name:<15} | {self.runs:^6} | {self.wickets:^7}"

class Team:
    def __init__(self, name):
        self.name = name
        self.players = {}

    def add_player(self, player_name):
        if player_name not in self.players:
            self.players[player_name] = Player(player_name)

    def get_player(self, player_name):
        return self.players.get(player_name)

    def team_stats(self):
        header = f"{'Player':<15} | {'Runs':^6} | {'Wickets':^7}\n" + "-" * 35
        stats = "\n".join(str(p) for p in self.players.values())
        return f"Team: {self.name}\n{header}\n{stats}\n"

class StatsManager:
    def __init__(self):
        self.teams = {}

    def add_team(self, team_name):
        if team_name not in self.teams:
            self.teams[team_name] = Team(team_name)

    def add_player(self, team_name, player_name):
        self.add_team(team_name)
        self.teams[team_name].add_player(player_name)

    def record_runs(self, team_name, player_name, runs):
        self.add_player(team_name, player_name)
        self.teams[team_name].get_player(player_name).add_runs(runs)

    def record_wicket(self, team_name, player_name):
        self.add_player(team_name, player_name)
        self.teams[team_name].get_player(player_name).add_wicket()

    def show_stats(self):
        for team in self.teams.values():
            print(team.team_stats())

    def save_stats(self, filename):
        with open(filename, "w") as f:
            for team in self.teams.values():
                for player in team.players.values():
                    line = f"{team.name},{player.name},{player.runs},{player.wickets}\n"
                    f.write(line)

    def load_stats(self, filename):
        if not os.path.exists(filename):
            print("No stats file found.")
            return
        self.teams.clear()
        with open(filename) as f:
            for line in f:
                team_name, player_name, runs, wickets = line.strip().split(",")
                self.add_player(team_name, player_name)
                player = self.teams[team_name].get_player(player_name)
                player.runs = int(runs)
                player.wickets = int(wickets)

def main():
    stats = StatsManager()
    filename = "cricket_stats.txt"
    stats.load_stats(filename)

    while True:
        print("\n--- Cricket Stats CLI ---")
        print("1. Add Player")
        print("2. Record Runs")
        print("3. Record Wicket")
        print("4. Show Stats")
        print("5. Save Stats")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            team = input("Team name: ").strip()
            player = input("Player name: ").strip()
            stats.add_player(team, player)
            print(f"Added {player} to team {team}.")
        elif choice == '2':
            team = input("Team name: ").strip()
            player = input("Player name: ").strip()
            runs = int(input("Runs to add: ").strip())
            stats.record_runs(team, player, runs)
            print(f"Added {runs} runs to {player} ({team}).")
        elif choice == '3':
            team = input("Team name: ").strip()
            player = input("Player name: ").strip()
            stats.record_wicket(team, player)
            print(f"Added 1 wicket to {player} ({team}).")
        elif choice == '4':
            stats.show_stats()
        elif choice == '5':
            stats.save_stats(filename)
            print("Stats saved.")
        elif choice == '6':
            stats.save_stats(filename)
            print("Stats saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
