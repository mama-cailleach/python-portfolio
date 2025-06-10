import sys
from collections import defaultdict
import os
import csv

BALLS_PER_OVER = 6
MAX_OVERS = 2
MAX_BOWLER_OVERS = 1

def list_xi_files():
    teams_dir = os.path.join(os.path.dirname(__file__), "./teams")
    if not os.path.isdir(teams_dir):
        return []
    return [f for f in os.listdir(teams_dir) if f.endswith("_XI.csv")]

def load_xi(filepath):
    players = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            players.append({'number': int(row['number']), 'name': row['name']})
    return players

def choose_team_xi(label):
    xi_files = list_xi_files()
    if not xi_files:
        print("No starting XI files found. Please use the team manager to create/select your teams.")
        sys.exit(1)
    print(f"\nAvailable starting XIs for {label} team:")
    for idx, fname in enumerate(xi_files, 1):
        print(f"{idx}. {fname}")
    while True:
        sel = input(f"Select {label} team by number: ").strip()
        if sel.isdigit() and 1 <= int(sel) <= len(xi_files):
            xi_file = xi_files[int(sel)-1]
            break
        print("Invalid selection.")
    team_name = xi_file[:-7]  # Remove _XI.csv
    xi_path = os.path.join(os.path.dirname(__file__), "./teams", xi_file)
    players = load_xi(xi_path)
    team = Team(team_name)
    order = []
    for p in players:
        team.add_player(Player(p['number'], p['name']))
        order.append(p['number'])
    team.order = order  # Set batting order as per CSV
    return team

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
        columns = ["Player Name", "Dismissal", "Runs", "Balls", "4s", "6s", "SR"]
        print("{:<20}{:<25}{:>5}{:>6}{:>4}{:>4}{:>7}".format(*columns))
        did_not_bat = []
        for num in self.batting_team.order:
            p = self.batting_team.players[num]
            bat = p.batting
            # Only print if the player actually batted
            if bat['balls'] > 0 or bat['runs'] > 0 or bat['dismissal'] != 'not out':
                # Format dismissal to only show surnames for bowler/fielder, and always include bowler for c/lbw
                dismissal = bat['dismissal']
                if dismissal.startswith("c "):
                    # c Fielder b Bowler
                    parts = dismissal.split()
                    if len(parts) >= 4:
                        fielder_surname = parts[1].split()[-1]
                        bowler_surname = parts[3].split()[-1]
                        dismissal = f"c {fielder_surname} b {bowler_surname}"
                elif dismissal.startswith("lbw b "):
                    bowler_surname = dismissal.split()[-1]
                    dismissal = f"lbw b {bowler_surname}"
                elif dismissal.startswith("b "):
                    bowler_surname = dismissal.split()[-1]
                    dismissal = f"b {bowler_surname}"
                elif dismissal.startswith("run out("):
                    inside = dismissal[8:-1]
                    fielder_surname = inside.split()[-1]
                    dismissal = f"run out({fielder_surname})"
                # Count 4s and 6s for this batter
                fours = 0
                sixes = 0
                for be in self.balls:
                    if be.batter == p and be.event == "normal":
                        if be.runs == 4:
                            fours += 1
                        elif be.runs == 6:
                            sixes += 1
                sr = (bat['runs'] / bat['balls'] * 100) if bat['balls'] > 0 else 0.0
                print("{:<20}{:<25}{:>5}{:>6}{:>4}{:>4}{:>7.2f}".format(
                    p.name, dismissal, bat['runs'], bat['balls'],
                    fours, sixes, sr
                ))
            else:
                did_not_bat.append(p.name)
        # Extras
        extras_total = sum(self.extras.values())
        print("{:<20}{:>25}{:>5}".format("Extras", '', extras_total))
        # Total
        runs, wickets, overs, rr = self.get_score()
        # Calculate legal balls for overs display
        balls = sum(1 for be in self.balls if be.event not in ['wide', 'no ball'])
        full_overs = balls // BALLS_PER_OVER
        rem_balls = balls % BALLS_PER_OVER
        if rem_balls == 0:
            overs_str = f"{full_overs} Ov"
        else:
            overs_str = f"{full_overs}.{rem_balls} Ov"
        print(f"\nTotal: {overs_str} (RR: {rr:.2f}) {runs}/{wickets}")
        # Did not bat
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
        columns = ["Bowler", "Overs", "M", "Runs", "Wkts", "Econ", "Dots", "4s", "6s", "Wd", "NB"]
        print("{:<20}{:>6}{:>8}{:>6}{:>6}{:>7}{:>6}{:>4}{:>4}{:>7}{:>8}".format(*columns))
        for num, p in self.bowling_team.players.items():
            if p.bowling['balls'] == 0:
                continue
            balls = p.bowling['balls']
            full_overs = balls // BALLS_PER_OVER
            rem_balls = balls % BALLS_PER_OVER
            if rem_balls == 0:
                overs = f"{full_overs}.0"
            else:
                overs = f"{full_overs}.{rem_balls}"
            maidens = p.bowling['maidens']
            runs = p.bowling['runs']
            wkts = p.bowling['wickets']
            econ = (runs / (balls/6)) if balls else 0
            dots = p.bowling['dots']
            # Count 4s and 6s for this bowler
            fours = 0
            sixes = 0
            for be in self.balls:
                if be.bowler == p and be.event == "normal":
                    if be.runs == 4:
                        fours += 1
                    elif be.runs == 6:
                        sixes += 1
            wides = p.bowling['wides']
            noballs = p.bowling['noballs']
            print("{:<20}{:>6}{:>8}{:>6}{:>6}{:>7.2f}{:>6}{:>4}{:>4}{:>7}{:>8}".format(
                p.name, overs, maidens, runs, wkts, econ, dots, fours, sixes, wides, noballs
            ))
        print()

def input_team(team_label):
    print(f"Do you want to (1) input {team_label} team manually or (2) load from file?")
    choice = input("Enter 1 or 2: ").strip()
    teams_dir = os.path.join(os.path.dirname(__file__), "./teams")
    os.makedirs(teams_dir, exist_ok=True)
    if choice == "2":
        while True:
            filename = input("Enter filename to load team from (just the file name, no path): ").strip()
            filepath = os.path.join(teams_dir, filename)
            if not os.path.isfile(filepath):
                print("File not found, try again.")
                continue
            with open(filepath, "r") as f:
                lines = [line.strip() for line in f if line.strip()]
            if len(lines) != 11:
                print("File must have 11 players.")
                continue
            name = os.path.splitext(os.path.basename(filename))[0]
            team = Team(name)
            for line in lines:
                try:
                    number, first, last = [x.strip() for x in line.split(",")]
                    number = int(number)
                    team.add_player(Player(number, f"{first} {last}"))
                except Exception:
                    print("Invalid line:", line)
                    return input_team(team_label)
            print(f"Loaded team '{team.name}':")
            for num, p in sorted(team.players.items()):
                print(f"{num}: {p.name}")
            return team
    # Manual input
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
                pname = input(f"Enter player {i+1} name and surname: ")
                team.add_player(Player(number, pname))
                break
            except Exception:
                print("you can't do that try again.")
    print(f"\n{name} team:")
    for num, p in sorted(team.players.items()):
        print(f"{num}: {p.name}")
    save = input("Save this team to file? (y/n): ").strip().lower()
    if save == "y":
        fname = input("Enter filename to save team (just the file name, no path): ").strip()
        filepath = os.path.join(teams_dir, fname)
        with open(filepath, "w") as f:
            for num, p in sorted(team.players.items()):
                parts = p.name.split()
                first = parts[0]
                last = " ".join(parts[1:]) if len(parts) > 1 else ""
                f.write(f"{num},{first},{last}\n")
        print(f"Team saved to {filepath}")
    return team

def select_openers(team):
    print(f"Select opening batters. Enter two numbers separated by space (choose by order number):")
    # Display players in XI order
    #for idx, num in enumerate(team.order, 1):
    #    p = team.players[num]
    #    print(f"{idx}: {num} {p.name}")
    while True:
        try:
            openers_idx = list(map(int, input().split()))
            if len(openers_idx) != 2 or openers_idx[0] == openers_idx[1]:
                print("you can't do that try again.")
                continue
            if not all(1 <= idx <= len(team.order) for idx in openers_idx):
                print("you can't do that try again.")
                continue
            openers = [team.order[idx-1] for idx in openers_idx]
            # Set openers as first in batting order
            team.order = openers + [n for n in team.order if n not in openers]
            return openers
        except Exception:
            print("you can't do that try again.")

def select_bowler(bowling_team, over, prev_bowler, bowler_overs):
    print(f"\nSelect bowler for over {over+1} from {bowling_team.name}:")
    eligible = []
    for idx, num in enumerate(bowling_team.order, 1):
        p = bowling_team.players[num]
        overs_bowled = len(bowler_overs[num])
        last_bowled = bowler_overs[num][-1] if bowler_overs[num] else -2
        can_bowl = overs_bowled < MAX_BOWLER_OVERS and (last_bowled < over-1 or last_bowled == -2)
        print(f"{idx}: {num} {p.name} - {overs_bowled} overs bowled", "(resting)" if not can_bowl else "")
        if can_bowl:
            eligible.append(idx)
    while True:
        try:
            sel = int(input("Enter order number of bowler: "))
            if sel not in eligible:
                print("you can't do that try again.")
                continue
            bowler_num = bowling_team.order[sel-1]
            return bowler_num
        except Exception:
            print("you can't do that try again.")

def input_ball(batters, bowler, over_num=None, ball_num=None, team=None):
    # Defensive: handle if a batter is None (all out)
    if batters[0] is None or batters[1] is None:
        print("No more batters available.")
        return 0, "end", [], False
    if over_num is not None and ball_num is not None:
        prompt_prefix = f"{over_num}.{ball_num} ov (0-6=runs scored, w=wicket, wd=wide, nb=no ball, b=bye, lb=leg bye): "
    else:
        prompt_prefix = "Event (0-6, w=wicket, wd=wide, nb=no ball, b=bye, lb=leg bye): "
    print(f"Striker: {batters[0].name}, Non-striker: {batters[1].name}, Bowler: {bowler.name}")
    event = input(prompt_prefix).strip()
    runs, event_type, fielders = 0, "normal", []
    swapped = False
    if event in ['w', 'W']:
        wicket_type = input("Wicket type (bowled, caught, lbw, run out): ").lower()
        if wicket_type == "bowled":
            event_type = "wicket"
            fielders = [bowler.name]
        elif wicket_type == "caught":
            fielder_num = int(input("Fielder shirt number: "))
            fielder = team.get_player(fielder_num).name if team and fielder_num in team.players else str(fielder_num)
            event_type = "wicket"
            fielders = [fielder, bowler.name]
        elif wicket_type == "lbw":
            event_type = "wicket"
            fielders = ["lbw", bowler.name]
        elif wicket_type == "run out":
            fielder_num = int(input("Fielder shirt number: "))
            fielder = team.get_player(fielder_num).name if team and fielder_num in team.players else str(fielder_num)
            event_type = "wicket"
            fielders = [fielder]
        else:
            print("you can't do that try again.")
            return input_ball(batters, bowler, over_num, ball_num, team)
    elif event == "wd":
        try:
            runs = int(input("Runs on wide (default 1): ") or "1")
            event_type = "wide"
        except:
            print("you can't do that try again.")
            return input_ball(batters, bowler, over_num, ball_num, team)
    elif event == "nb":
        try:
            runs = int(input("Runs on no ball (default 1): ") or "1")
            event_type = "no ball"
        except:
            print("you can't do that try again.")
            return input_ball(batters, bowler, over_num, ball_num, team)
    elif event == "b":
        try:
            runs = int(input("Byes: "))
            event_type = "bye"
            swap = input("Did the batters swap ends? (y/n): ").strip().lower()
            swapped = (swap == "y")
        except:
            print("you can't do that try again.")
            return input_ball(batters, bowler, over_num, ball_num, team)
    elif event == "lb":
        try:
            runs = int(input("Leg byes: "))
            event_type = "leg bye"
            swap = input("Did the batters swap ends? (y/n): ").strip().lower()
            swapped = (swap == "y")
        except:
            print("you can't do that try again.")
            return input_ball(batters, bowler, over_num, ball_num, team)
    else:
        try:
            runs = int(event)
            if runs < 0 or runs > 6:
                print("you can't do that try again.")
                return input_ball(batters, bowler, over_num, ball_num, team)
        except:
            print("you can't do that try again.")
            return input_ball(batters, bowler, over_num, ball_num, team)
    return runs, event_type, fielders, swapped

def main():
    print("Cricket T20 Scorecard Creator/Analyzer\n")
    ready = input("Do you have your starting XIs ready? (y/n): ").strip().lower()
    if ready != "y":
        print("Please use the team manager (team_utils.py) to create/select your teams and starting XIs before running the scorecard generator.")
        sys.exit(0)
    print("\nChoose teams for the match:")
    team1 = choose_team_xi("first")
    team2 = choose_team_xi("second")

    # Toss logic
    print("\nWho won the toss?")
    print(f"1. {team1.name}")
    print(f"2. {team2.name}")
    while True:
        toss_winner = input("Enter number: ").strip()
        if toss_winner == "1":
            toss_team = team1
            toss_loser = team2
            break
        elif toss_winner == "2":
            toss_team = team2
            toss_loser = team1
            break
        else:
            print("Invalid selection.")
    print(f"\nWhat does {toss_team.name} choose?")
    print("1. Bat first")
    print("2. Bowl first")
    while True:
        toss_choice = input("Enter number: ").strip()
        if toss_choice == "1":
            batting_first = toss_team
            bowling_first = toss_loser
            break
        elif toss_choice == "2":
            batting_first = toss_loser
            bowling_first = toss_team
            break
        else:
            print("Invalid selection.")

    # Show available players for opening selection
    print(f"\nFirst Innings: {batting_first.name} Batting")
    print("Players available to open the batting:")
    for idx, num in enumerate(batting_first.order, 1):
        p = batting_first.players[num]
        print(f"{idx}: {num} {p.name}")

    innings1 = Innings(batting_first, bowling_first)

    # Batting order
    openers = select_openers(batting_first)
    striker, non_striker = batting_first.players[openers[0]], batting_first.players[openers[1]]
    current_batters = [striker, non_striker]
    batters_yet = [num for num in batting_first.order if num not in batting_first.order[:2]]
    bowler_overs = defaultdict(list)
    wickets = 0
    over = 0
    prev_bowler = None
    while over < MAX_OVERS and wickets < 10:
        bowler_num = select_bowler(bowling_first, over, prev_bowler, bowler_overs)
        bowler = bowling_first.players[bowler_num]
        balls_this_over = 0
        over_runs = 0
        over_dots = 0
        over_start_balls = len(innings1.balls)
        legal_balls = 0
        ball = 1
        over_ended_early = False  # PATCH: flag to indicate early over end
        while legal_balls < 6:
            # Only break if 10 wickets have fallen or both batters are None
            if wickets == 10 or current_batters[0] is None or current_batters[1] is None:
                over_ended_early = True  # PATCH
                break
            result = input_ball(current_batters, bowler, over, ball, bowling_first)
            if len(result) == 4:
                runs, event_type, fielders, swapped = result
            else:
                runs, event_type, fielders = result
                swapped = False
            if event_type == "end":
                over_ended_early = True  # PATCH
                break
            batter = current_batters[0]
            event = BallEvent(over, ball, bowler, batter, runs, event_type, fielders)
            innings1.add_ball(event)
            batter.batted = True
            bowler.bowled = True
            balls_this_over += 1
            is_legal = event_type not in ["wide", "no ball"]
            if event_type == "normal":
                batter.batting['runs'] += runs
                batter.batting['balls'] += 1
                if runs == 4: bowler.bowling['4s'] += 1
                if runs == 6: bowler.bowling['6s'] += 1
                if runs == 0: 
                    bowler.bowling['dots'] += 1
                    over_dots += 1
                bowler.bowling['balls'] += 1
                bowler.bowling['runs'] += runs
                if runs == 4: bowler.bowling['4s'] += 1
                if runs == 6: bowler.bowling['6s'] += 1
                over_runs += runs
                if runs % 2 == 1:
                    current_batters.reverse()
                legal_balls += 1
                ball += 1
            elif event_type == "wide":
                innings1.extras['wides'] += runs
                bowler.bowling['wides'] += runs
                bowler.bowling['runs'] += runs
                # PATCH: do NOT increment legal_balls for wides
            elif event_type == "no ball":
                innings1.extras['no balls'] += runs
                bowler.bowling['noballs'] += runs
                bowler.bowling['runs'] += runs
                # PATCH: do NOT increment legal_balls for no balls
            elif event_type == "bye":
                innings1.extras['byes'] += runs
                batter.batting['balls'] += 1
                bowler.bowling['balls'] += 1
                over_runs += runs
                if swapped:
                    current_batters.reverse()
                legal_balls += 1
                ball += 1
            elif event_type == "leg bye":
                innings1.extras['leg byes'] += runs
                batter.batting['balls'] += 1
                bowler.bowling['balls'] += 1
                over_runs += runs
                if swapped:
                    current_batters.reverse()
                legal_balls += 1
                ball += 1
            elif event_type == "wicket":
                batter.batting['balls'] += 1
                bowler.bowling['balls'] += 1
                # Fix dismissal string logic
                if len(fielders) == 2:
                    fielder_surname = fielders[0].split()[-1]
                    bowler_surname = bowler.name.split()[-1]
                    batter.batting['dismissal'] = f"c {fielder_surname} b {bowler_surname}"
                    bowler.bowling['wickets'] += 1
                elif len(fielders) >= 2 and fielders[0] == "lbw":
                    bowler_surname = bowler.name.split()[-1]
                    batter.batting['dismissal'] = f"lbw b {bowler_surname}"
                    bowler.bowling['wickets'] += 1
                elif fielders and "run out" in fielders[0].lower():
                    batter.batting['dismissal'] = f"run out({fielders[0]})"
                elif len(fielders) == 1:
                    if " " in fielders[0] and fielders[0] != bowler.name:
                        fielder_surname = fielders[0].split()[-1]
                        batter.batting['dismissal'] = f"run out({fielder_surname})"
                    else:
                        bowler_surname = fielders[0].split()[-1]
                        batter.batting['dismissal'] = f"b {bowler_surname}"
                        bowler.bowling['wickets'] += 1
                else:
                    batter.batting['dismissal'] = "unknown"
                runs_total, _, _, _ = innings1.get_score()
                curr_wickets = wickets + 1
                print(f"\nWICKET! Score: {runs_total}-{curr_wickets} | {batter.name} {batter.batting['runs']}({batter.batting['balls']})")
                wickets += 1
                innings1.fall_of_wickets.append((runs_total, batter.name, bowler.name, over + ball / 10))
                legal_balls += 1
                ball += 1
                if wickets == 10:
                    current_batters[0] = None
                    current_batters[1] = None
                    over_ended_early = True  # PATCH
                    break

                # After a wicket has fallen, find batters who are neither out nor the non-striker
                non_striker = current_batters[1]
                batters_batted = [b.number for b in batting_first.players.values() if b.batting['balls'] > 0 or b.batting['dismissal'] != 'not out']
                # Correct: Exclude the non-striker from batters_yet, regardless of whether they've faced a ball yet
                batters_yet = [
                num for num in batting_first.order
                if num not in batters_batted and (non_striker is None or num != non_striker.number)
                ]
                if batters_yet:
                    print("Choose next batter in from:")
                    for idx, num in enumerate(batters_yet, 1):
                        p = batting_first.players[num]
                        print(f"{idx}: {num} {p.name}")
                    while True:
                        try:
                            next_batter_idx = int(input("Enter order number of next batter: "))
                            if not (1 <= next_batter_idx <= len(batters_yet)):
                                print("you can't do that try again.")
                                continue
                            next_batter_num = batters_yet[next_batter_idx-1]
                            break
                        except:
                            print("you can't do that try again.")
                    current_batters[0] = batting_first.players[next_batter_num]
                else:
                    current_batters[0] = None
                    current_batters[1] = None
                    over_ended_early = True  # PATCH
                    break
        if over_ended_early:
            print("OVER ENDED EARLY (all out, no batters, or innings ended).")  # PATCH
        else:
            print("OVER FINISHED.")
        bowler_overs[bowler_num].append(over)
        if over_runs == 0:
            bowler.bowling['maidens'] += 1
        prev_bowler = bowler_num
        over += 1
        if over > 0 and current_batters[0] and current_batters[1]:
            current_batters.reverse()  # Swap ends    

    innings1.print_batting_scorecard()
    innings1.print_bowling_scorecard()

if __name__ == "__main__":
    main()