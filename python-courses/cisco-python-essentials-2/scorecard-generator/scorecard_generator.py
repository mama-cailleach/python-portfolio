import sys
from collections import defaultdict

BALLS_PER_OVER = 6
MAX_OVERS = 20
MAX_BOWLER_OVERS = 4

def safe_int(prompt, valid=None):
    while True:
        val = input(prompt)
        try:
            val_int = int(val)
            if valid and val_int not in valid:
                print("you can't do that try again.")
                continue
            return val_int
        except:
            print("you can't do that try again.")

def safe_choice(prompt, options):
    while True:
        val = input(prompt)
        if val in options:
            return val
        print("you can't do that try again.")

class Player:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.batting = {
            'runs': 0, 'balls': 0, '4s': 0, '6s': 0,
            'SR': 0.0, 'dismissal': 'not out'
        }
        self.bowling = {
            'balls': 0, 'runs': 0, 'wickets': 0, 'maidens': 0,
            'dots': 0, '4s': 0, '6s': 0, 'wides': 0, 'noballs': 0
        }
        self.batted = False
        self.bowled = False

    def __str__(self):
        return f"{self.number} {self.name}"

class Team:
    def __init__(self, name):
        self.name = name
        self.players = {}  # number: Player
        self.order = []    # batting order
        self.bowler_order = []

    def add_player(self, player):
        self.players[player.number] = player

    def get_player(self, number):
        return self.players[number]

    def all_players(self):
        return [self.players[num] for num in sorted(self.players)]

    def get_batters(self):
        return [self.players[num] for num in self.order]

    def get_bowlers(self):
        return [self.players[num] for num in self.bowler_order]

class BallEvent:
    def __init__(self, over, ball, bowler, batter, runs, event, fielders=None):
        self.over = over
        self.ball = ball
        self.bowler = bowler  # Player obj
        self.batter = batter  # Player obj
        self.runs = runs
        self.event = event  # normal, wicket, wide, no ball, bye, leg bye
        self.fielders = fielders or []  # for catch/run out

class Innings:
    def __init__(self, batting_team, bowling_team):
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.balls = []  # list of BallEvent
        self.current_batters = []
        self.dismissed = []
        self.did_not_bat = []
        self.fall_of_wickets = []
        self.extras = defaultdict(int)  # byes, leg byes, wides, no balls
        self.bowler_overs = defaultdict(list)  # bowler.number : list of over numbers

    def add_ball(self, ball_event):
        self.balls.append(ball_event)

    def get_score(self):
        runs = sum(be.runs for be in self.balls if be.event not in ['wide', 'no ball'])
        runs += self.extras['wides'] + self.extras['no balls'] + self.extras['byes'] + self.extras['leg byes']
        wickets = len(self.fall_of_wickets)
        balls = sum(1 for be in self.balls if be.event not in ['wide', 'no ball'])
        overs = balls // BALLS_PER_OVER + (balls % BALLS_PER_OVER) / 10
        rr = runs / (balls / 6) if balls else 0
        return runs, wickets, overs, rr

    def print_batting_scorecard(self):
        print(f"\nBatting: {self.batting_team.name}")
        columns = ["No", "Player Name", "Dismissal", "Runs", "Balls", "4s", "6s", "SR"]
        print("{:<4}{:<20}{:<25}{:>5}{:>6}{:>4}{:>4}{:>7}".format(*columns))
        for num in self.batting_team.order:
            p = self.batting_team.players[num]
            bat = p.batting
            balls = bat['balls']
            sr = (bat['runs']*100/balls if balls else 0)
            print("{:<4}{:<20}{:<25}{:>5}{:>6}{:>4}{:>4}{:>7.2f}".format(
                p.number, p.name, bat['dismissal'], bat['runs'], balls,
                bat['4s'], bat['6s'], sr
            ))
        # Extras
        extras_total = sum(self.extras.values())
        print("{:<4}{:<20}{:>25}{:>5}".format('', "Extras", '', extras_total))
        # Total
        runs, wickets, overs, rr = self.get_score()
        print("\nTotal: {} Ov ({:.2f}) Runs/{}".format(runs, rr, wickets))
        # Did not bat
        did_not_bat = [p.name for n, p in self.batting_team.players.items() if n not in self.batting_team.order]
        if did_not_bat:
            print("Did not bat: " + ", ".join(did_not_bat))
        # Fall of wickets
        print("Fall of wickets:")
        for i, fw in enumerate(self.fall_of_wickets, 1):
            runs, batsman, bowler, over = fw
            print(f" {i}-{runs} ({bowler}, {over:.1f} ov)", end=",")
        print("\n")

    def print_bowling_scorecard(self):
        print(f"Bowling: {self.bowling_team.name}")
        columns = ["Bowler", "Overs", "Maidens", "Runs", "Wkts", "Econ", "Dots", "4s", "6s", "Wides", "Noballs"]
        print("{:<20}{:>6}{:>8}{:>6}{:>6}{:>7}{:>6}{:>4}{:>4}{:>7}{:>8}".format(*columns))
        for num, p in self.bowling_team.players.items():
            balls = p.bowling['balls']
            overs = balls // BALLS_PER_OVER + (balls % BALLS_PER_OVER) / 10
            maidens = p.bowling['maidens']
            runs = p.bowling['runs']
            wkts = p.bowling['wickets']
            econ = (runs / (balls/6)) if balls else 0
            dots = p.bowling['dots']
            f4s = p.bowling['4s']
            s6s = p.bowling['6s']
            wides = p.bowling['wides']
            noballs = p.bowling['noballs']
            print("{:<20}{:>6.1f}{:>8}{:>6}{:>6}{:>7.2f}{:>6}{:>4}{:>4}{:>7}{:>8}".format(
                p.name, overs, maidens, runs, wkts, econ, dots, f4s, s6s, wides, noballs
            ))
        print()

def input_team(team_label):
    name = input(f"Enter {team_label} team name: ")
    team = Team(name)
    print(f"Enter the 11 players for {name}:")
    for i in range(11):
        while True:
            try:
                number = int(input(f"Enter player {i+1} shirt number: "))
                if number in team.players:
                    print("you can't do that try again.")
                    continue
                pname = input(f"Enter player {i+1} name: ")
                team.add_player(Player(number, pname))
                break
            except Exception:
                print("you can't do that try again.")
    return team

def select_openers(team):
    print(f"Select opening batters for {team.name}. Enter shirt numbers separated by space: ")
    while True:
        try:
            openers = list(map(int, input().split()))
            if len(openers) != 2 or openers[0] == openers[1]:
                print("you can't do that try again.")
                continue
            if not all(num in team.players for num in openers):
                print("you can't do that try again.")
                continue
            team.order.extend(openers)
            return openers
        except Exception:
            print("you can't do that try again.")

def select_bowler(bowling_team, over, prev_bowler, bowler_overs):
    print(f"\nSelect bowler for over {over+1} from {bowling_team.name}:")
    eligible = []
    for num, p in bowling_team.players.items():
        overs_bowled = len(bowler_overs[num])
        last_bowled = bowler_overs[num][-1] if bowler_overs[num] else -2
        can_bowl = overs_bowled < MAX_BOWLER_OVERS and (last_bowled < over-1 or last_bowled == -2)
        print(f"{num}: {p.name} - {overs_bowled} overs bowled", "(resting)" if not can_bowl else "")
        if can_bowl:
            eligible.append(num)
    while True:
        try:
            sel = int(input("Enter shirt number of bowler: "))
            if sel not in eligible:
                print("you can't do that try again.")
                continue
            return sel
        except Exception:
            print("you can't do that try again.")

def input_ball(batters, bowler):
    print(f"Striker: {batters[0].name}, Non-striker: {batters[1].name}, Bowler: {bowler.name}")
    event = input("Event (0-6, w=wicket, wd=wide, nb=no ball, b=bye, lb=leg bye): ").strip()
    runs, event_type, fielders = 0, "normal", []
    if event in ['w', 'W']:
        wicket_type = input("Wicket type (bowled, caught, lbw, run out): ").lower()
        if wicket_type == "bowled":
            event_type = "wicket"
            fielders = [bowler.name]
        elif wicket_type == "caught":
            fielder = input("Fielder surname: ")
            event_type = "wicket"
            fielders = [fielder, bowler.name]
        elif wicket_type == "lbw":
            event_type = "wicket"
            fielders = [bowler.name]
        elif wicket_type == "run out":
            fielder = input("Fielder surname: ")
            event_type = "wicket"
            fielders = [fielder]
        else:
            print("you can't do that try again.")
            return input_ball(batters, bowler)
    elif event == "wd":
        try:
            runs = int(input("Runs on wide (default 1): ") or "1")
            event_type = "wide"
        except:
            print("you can't do that try again.")
            return input_ball(batters, bowler)
    elif event == "nb":
        try:
            runs = int(input("Runs on no ball (default 1): ") or "1")
            event_type = "no ball"
        except:
            print("you can't do that try again.")
            return input_ball(batters, bowler)
    elif event == "b":
        try:
            runs = int(input("Byes: "))
            event_type = "bye"
        except:
            print("you can't do that try again.")
            return input_ball(batters, bowler)
    elif event == "lb":
        try:
            runs = int(input("Leg byes: "))
            event_type = "leg bye"
        except:
            print("you can't do that try again.")
            return input_ball(batters, bowler)
    else:
        try:
            runs = int(event)
            if runs < 0 or runs > 6:
                print("you can't do that try again.")
                return input_ball(batters, bowler)
        except:
            print("you can't do that try again.")
            return input_ball(batters, bowler)
    return runs, event_type, fielders

def main():
    print("Cricket T20 Scorecard Creator/Analyzer\n")
    team1 = input_team("first")
    team2 = input_team("second")
    print("\nFirst Innings: " + team1.name + " Batting")
    innings1 = Innings(team1, team2)

    # Batting order
    openers = select_openers(team1)
    striker, non_striker = team1.players[openers[0]], team1.players[openers[1]]
    team1.order.extend([openers[0], openers[1]])
    current_batters = [striker, non_striker]
    batters_yet = [num for num in team1.players if num not in team1.order]
    bowler_overs = defaultdict(list)
    wickets = 0
    over = 0
    prev_bowler = None
    while over < MAX_OVERS and wickets < 10:
        bowler_num = select_bowler(team2, over, prev_bowler, bowler_overs)
        bowler = team2.players[bowler_num]
        balls_this_over = 0
        over_runs = 0
        over_dots = 0
        over_start_balls = len(innings1.balls)
        for ball in range(1, 7):
            if wickets == 10:
                break
            runs, event_type, fielders = input_ball(current_batters, bowler)
            batter = current_batters[0]
            event = BallEvent(over, ball, bowler, batter, runs, event_type, fielders)
            innings1.add_ball(event)
            batter.batted = True
            bowler.bowled = True
            balls_this_over += 1
            if event_type == "normal":
                batter.batting['runs'] += runs
                batter.batting['balls'] += 1
                if runs == 4: batter.batting['4s'] += 1
                if runs == 6: batter.batting['6s'] += 1
                if runs == 0: 
                    bowler.bowling['dots'] += 1
                    over_dots += 1
                bowler.bowling['balls'] += 1
                bowler.bowling['runs'] += runs
                if runs == 4: bowler.bowling['4s'] += 1
                if runs == 6: bowler.bowling['6s'] += 1
                over_runs += runs
                # Swap on odd runs
                if runs % 2 == 1:
                    current_batters.reverse()
            elif event_type == "wide":
                innings1.extras['wides'] += runs
                bowler.bowling['wides'] += runs
                bowler.bowling['runs'] += runs
                balls_this_over -= 1  # Does not count as legal ball
            elif event_type == "no ball":
                innings1.extras['no balls'] += runs
                bowler.bowling['noballs'] += runs
                bowler.bowling['runs'] += runs
                balls_this_over -= 1
            elif event_type == "bye":
                innings1.extras['byes'] += runs
                batter.batting['balls'] += 1
                bowler.bowling['balls'] += 1
                over_runs += runs
            elif event_type == "leg bye":
                innings1.extras['leg byes'] += runs
                batter.batting['balls'] += 1
                bowler.bowling['balls'] += 1
                over_runs += runs
            elif event_type == "wicket":
                batter.batting['balls'] += 1
                bowler.bowling['balls'] += 1
                # Dismissal string
                if len(fielders) == 2:
                    batter.batting['dismissal'] = f"c {fielders[0]} b {fielders[1]}"
                elif fielders and "lbw" in fielders[0].lower():
                    batter.batting['dismissal'] = f"lbw b {bowler.name.split()[-1]}"
                elif fielders and "run out" in fielders[0].lower():
                    batter.batting['dismissal'] = f"run out({fielders[0]})"
                elif len(fielders) == 1:
                    batter.batting['dismissal'] = f"b {fielders[0].split()[-1]}"
                else:
                    batter.batting['dismissal'] = "unknown"
                bowler.bowling['wickets'] += 1
                wickets += 1
                runs_total, wkts, _, _ = innings1.get_score()
                # Show live wicket info
                print(f"\nWICKET! Score: {runs_total}-{wkts} | {batter.name} {batter.batting['runs']}({batter.batting['balls']})")
                # Choose next batter
                if batters_yet:
                    print("Choose next batter in from:")
                    for n in batters_yet:
                        print(f"{n}: {team1.players[n].name}")
                    while True:
                        try:
                            next_batter_num = int(input("Enter shirt number of next batter: "))
                            if next_batter_num not in batters_yet:
                                print("you can't do that try again.")
                                continue
                            break
                        except:
                            print("you can't do that try again.")
                    team1.order.append(next_batter_num)
                    current_batters[0] = team1.players[next_batter_num]
                    batters_yet.remove(next_batter_num)
                else:
                    current_batters[0] = None
                innings1.fall_of_wickets.append((runs_total, batter.name, bowler.name, over + ball / 10))
            if wickets == 10:
                break
        bowler_overs[bowler_num].append(over)
        if over_runs == 0:
            bowler.bowling['maidens'] += 1
        prev_bowler = bowler_num
        over += 1
        current_batters.reverse()  # Swap ends

    innings1.print_batting_scorecard()
    innings1.print_bowling_scorecard()

if __name__ == "__main__":
    main()
