from .models import Player, Team

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

def get_display_name(team, num):
    p = team.players[num]
    name = p.name
    is_captain = hasattr(team, 'captain_number') and num == team.captain_number
    is_keeper = hasattr(team, 'wicketkeeper_number') and num == team.wicketkeeper_number
    if is_captain and is_keeper:
        name += " (c)†"
    elif is_captain:
        name += " (c)"
    elif is_keeper:
        name += " †"
    return name

def select_openers(team):
    print(f"Select opening batters. Enter two numbers separated by space (choose by order number):")
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
            team.order = openers + [n for n in team.order if n not in openers]
            return openers
        except Exception:
            print("you can't do that try again.")

def select_bowler(bowling_team, over, prev_bowler, bowler_overs):
    from .models import MAX_BOWLER_OVERS
    print(f"\nSelect bowler for over {over+1} from {bowling_team.name}:")
    eligible = []
    for idx, num in enumerate(bowling_team.order, 1):
        overs_bowled = len(bowler_overs[num])
        last_bowled = bowler_overs[num][-1] if bowler_overs[num] else -2
        can_bowl = overs_bowled < MAX_BOWLER_OVERS and (last_bowled < over-1 or last_bowled == -2)
        print(f"{idx}: {num} {get_display_name(bowling_team, num)} - {overs_bowled} overs bowled", "(resting)" if not can_bowl else "")
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

def handle_no_ball_outcome(outcome, batters, bowler, team, over_num, ball_num):
    runs = 1
    event_type = "no ball"
    fielders = []
    swapped = False

    if outcome in ['0', '']:
        return runs, event_type, fielders, swapped
    elif outcome.isdigit() and int(outcome) in range(1, 7):
        bat_runs = int(outcome)
        return (runs + bat_runs), "no ball_runs", fielders, (bat_runs % 2 == 1)
    elif outcome == 'bye':
        print("How many byes?")
        bye_runs = int(input("> "))
        swapped = (bye_runs % 2 == 1)
        return (runs + bye_runs), "no ball_bye", fielders, swapped
    elif outcome in ['leg bye', 'leg byes']:
        print("How many leg byes?")
        lb_runs = int(input("> "))
        swapped = (lb_runs % 2 == 1)
        return (runs + lb_runs), "no ball_leg_bye", fielders, swapped
    elif outcome == 'run out':
        print("How many runs completed before run out?")
        completed_runs = int(input("> "))
        swapped = (completed_runs % 2 == 1)
        print("Which batter was run out? (striker/non-striker)")
        out_batter = input("> ").strip().lower()
        if out_batter == 'striker':
            fielders = [batters[0].name]
        elif out_batter == 'non-striker':
            fielders = [batters[1].name]
        else:
            print("Invalid input.")
            return handle_no_ball_outcome(outcome, batters, bowler, team, over_num, ball_num)
        return (runs + completed_runs), "no ball_run_out", fielders, swapped
    else:
        print("Invalid input, please try again.")
        print("Valid options: 0-6, bye, leg bye, run out")
        new_outcome = input("> ").strip().lower()
        return handle_no_ball_outcome(new_outcome, batters, bowler, team, over_num, ball_num)

def input_ball(batters, bowler, over_num=None, ball_num=None, team=None):
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
        wicket_type = input("Wicket type (bowled, caught, lbw, run out, stumped): ").lower()
        if wicket_type == "bowled":
            event_type = "wicket"
            fielders = [bowler.name]
        elif wicket_type == "caught":
            fielder_input = input("Fielder shirt number (or 'bowler'): ").strip().lower()
            if fielder_input == "bowler":
                fielder = bowler.name
                is_c_and_b = True
            else:
                try:
                    fielder_num = int(fielder_input)
                    fielder = team.get_player(fielder_num).name if team and fielder_num in team.players else str(fielder_num)
                    is_c_and_b = (fielder_num == bowler.number)
                except:
                    print("you can't do that try again.")
                    return input_ball(batters, bowler, over_num, ball_num, team)
            event_type = "wicket"
            fielders = [(fielder, bowler.name, is_c_and_b)]
        elif wicket_type == "lbw":
            event_type = "wicket"
            fielders = ["lbw", bowler.name]
        elif wicket_type == "run out":
            fielder_num = int(input("Fielder shirt number: "))
            fielder = team.get_player(fielder_num).name if team and fielder_num in team.players else str(fielder_num)
            event_type = "wicket"
            fielders = [fielder]
        elif wicket_type == "stumped":
            if team and getattr(team, 'wicketkeeper_number', None) is not None:
                wicketkeeper = team.get_player(team.wicketkeeper_number).name
            else:
                print("No wicketkeeper set for this team.")
                return input_ball(batters, bowler, over_num, ball_num, team)
            event_type = "wicket"
            fielders = [wicketkeeper, bowler.name]
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
        print("No ball! 1 penalty run awarded (extra).")
        print("Please input if any extra runs or outcomes (0-6, bye, leg bye, run out):")
        outcome = input("> ").strip().lower()
        return handle_no_ball_outcome(outcome, batters, bowler, team, over_num, ball_num)
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