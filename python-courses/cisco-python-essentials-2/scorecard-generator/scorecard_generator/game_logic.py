from .models import BallEvent, Innings, Player, Team
from .scorecard import print_batting_scorecard, print_bowling_scorecard
from .input_handlers import input_ball, select_openers, select_bowler, get_display_name

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

def process_ball_event(
    event_type, runs, fielders, swapped, innings, bowler, batter,
    current_batters, wickets, over, ball_num, batting_team, over_runs,
    legal_balls, ball_number, batters_yet
):
    over_ended_early = False
    # Normal scoring ball
    if event_type == "normal":
        batter.batting['runs'] += runs
        batter.batting['balls'] += 1
        if runs == 4:
            bowler.bowling['4s'] += 1
        if runs == 6:
            bowler.bowling['6s'] += 1
        if runs == 0:
            bowler.bowling['dots'] += 1
        bowler.bowling['balls'] += 1
        bowler.bowling['runs'] += runs
        over_runs += runs
        if runs % 2 == 1:
            current_batters.reverse()
        legal_balls += 1
        ball_number += 1
    elif event_type == "wide":
        innings.extras['wides'] += runs
        bowler.bowling['wides'] += runs
        bowler.bowling['runs'] += runs
        # ball not counted as legal
    elif event_type == "no ball":
        innings.extras['no balls'] += 1
        bowler.bowling['noballs'] += 1
        bowler.bowling['runs'] += 1
        # ball not counted as legal
    elif event_type == "no ball_runs":
        penalty = 1
        bat_runs = runs - penalty
        innings.extras['no balls'] += penalty
        bowler.bowling['noballs'] += penalty
        bowler.bowling['runs'] += runs
        batter.batting['runs'] += bat_runs
        if bat_runs == 4:
            bowler.bowling['4s'] += 1
        if bat_runs == 6:
            bowler.bowling['6s'] += 1
        over_runs += runs
        if bat_runs % 2 == 1:
            current_batters.reverse()
        # ball not counted as legal
    elif event_type == "no ball_bye":
        penalty = 1
        bye_runs = runs - penalty
        innings.extras['no balls'] += penalty
        innings.extras['byes'] += bye_runs
        bowler.bowling['noballs'] += penalty
        bowler.bowling['runs'] += runs
        over_runs += runs
        if swapped:
            current_batters.reverse()
        # ball not counted as legal
    elif event_type == "no ball_leg_bye":
        penalty = 1
        lb_runs = runs - penalty
        innings.extras['no balls'] += penalty
        innings.extras['leg byes'] += lb_runs
        bowler.bowling['noballs'] += penalty
        bowler.bowling['runs'] += runs
        over_runs += runs
        if swapped:
            current_batters.reverse()
        # ball not counted as legal
    elif event_type == "no ball_run_out":
        penalty = 1
        completed_runs = runs - penalty
        innings.extras['no balls'] += penalty
        bowler.bowling['noballs'] += penalty
        bowler.bowling['runs'] += runs
        over_runs += runs
        if swapped:
            current_batters.reverse()
        out_batter_name = fielders[0]
        if out_batter_name == current_batters[0].name:
            out_idx = 0
        else:
            out_idx = 1
        out_batter = current_batters[out_idx]
        out_batter.batting['dismissal'] = f"run out({out_batter.name})"
        runs_total, _, _, _ = innings.get_score()
        curr_wickets = wickets + 1
        print(f"\nWICKET! Score: {runs_total}-{curr_wickets} | {out_batter.name} {out_batter.batting['runs']}({out_batter.batting['balls']})")
        wickets += 1
        innings.fall_of_wickets.append((runs_total, out_batter.name, bowler.name, over + ball_number / 10))
        # Replace out batter with new one, if any remain
        non_out_idx = 1 - out_idx
        survivor = current_batters[non_out_idx]
        batters_batted = [b.number for b in batting_team.players.values() if b.batting['balls'] > 0 or b.batting['dismissal'] != 'not out']
        batters_yet = [
            num for num in batting_team.order
            if num not in batters_batted and (survivor is None or num != survivor.number)
        ]
        if batters_yet:
            print("Choose next batter in from:")
            for idx, num in enumerate(batters_yet, 1):
                print(f"{idx}: {num} {get_display_name(batting_team, num)}")
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
            current_batters[out_idx] = batting_team.players[next_batter_num]
        else:
            current_batters[0] = None
            current_batters[1] = None
            over_ended_early = True
            return wickets, over_runs, legal_balls, ball_number, current_batters, batters_yet, over_ended_early
        # ball not counted as legal
    elif event_type == "bye":
        innings.extras['byes'] += runs
        batter.batting['balls'] += 1
        bowler.bowling['balls'] += 1
        over_runs += runs
        if swapped:
            current_batters.reverse()
        legal_balls += 1
        ball_number += 1
    elif event_type == "leg bye":
        innings.extras['leg byes'] += runs
        batter.batting['balls'] += 1
        bowler.bowling['balls'] += 1
        over_runs += runs
        if swapped:
            current_batters.reverse()
        legal_balls += 1
        ball_number += 1
    elif event_type == "wicket":
        batter.batting['balls'] += 1
        bowler.bowling['balls'] += 1
        # Handle c & b
        if len(fielders) == 1 and isinstance(fielders[0], tuple):
            fielder, bowler_name, is_c_and_b = fielders[0]
            bowler_surname = bowler.name.split()[-1]
            if is_c_and_b:
                batter.batting['dismissal'] = f"c & b {bowler_surname}"
            else:
                fielder_surname = fielder.split()[-1]
                batter.batting['dismissal'] = f"c {fielder_surname} b {bowler_surname}"
            bowler.bowling['wickets'] += 1
        elif len(fielders) >= 2 and fielders[0] == "lbw":
            bowler_surname = bowler.name.split()[-1]
            batter.batting['dismissal'] = f"lbw b {bowler_surname}"
            bowler.bowling['wickets'] += 1
        elif len(fielders) == 2:
            if ' ' in fielders[0] and fielders[0] != bowler.name and not (fielders[0] == "lbw"):
                wicketkeeper_surname = fielders[0].split()[-1]
                bowler_surname = bowler.name.split()[-1]
                if fielders[0] != bowler.name:
                    batter.batting['dismissal'] = f"st {wicketkeeper_surname} b {bowler_surname}"
                else:
                    fielder_surname = fielders[0].split()[-1]
                    batter.batting['dismissal'] = f"c {fielder_surname} b {bowler_surname}"
                bowler.bowling['wickets'] += 1
            else:
                fielder_surname = fielders[0].split()[-1]
                bowler_surname = bowler.name.split()[-1]
                batter.batting['dismissal'] = f"c {fielder_surname} b {bowler_surname}"
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
        runs_total, _, _, _ = innings.get_score()
        curr_wickets = wickets + 1
        print(f"\nWICKET! Score: {runs_total}-{curr_wickets} | {batter.name} {batter.batting['runs']}({batter.batting['balls']})")
        wickets += 1
        innings.fall_of_wickets.append((runs_total, batter.name, bowler.name, over + ball_number / 10))
        legal_balls += 1
        ball_number += 1
        if wickets == 10:
            current_batters[0] = None
            current_batters[1] = None
            over_ended_early = True
            return wickets, over_runs, legal_balls, ball_number, current_batters, batters_yet, over_ended_early
        non_striker = current_batters[1]
        batters_batted = [b.number for b in batting_team.players.values() if b.batting['balls'] > 0 or b.batting['dismissal'] != 'not out']
        batters_yet = [
            num for num in batting_team.order
            if num not in batters_batted and (non_striker is None or num != non_striker.number)
        ]
        if batters_yet:
            print("Choose next batter in from:")
            for idx, num in enumerate(batters_yet, 1):
                print(f"{idx}: {num} {get_display_name(batting_team, num)}")
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
            current_batters[0] = batting_team.players[next_batter_num]
        else:
            current_batters[0] = None
            current_batters[1] = None
            over_ended_early = True
            return wickets, over_runs, legal_balls, ball_number, current_batters, batters_yet, over_ended_early
    else:
        pass  # Unhandled event type, do nothing
    return wickets, over_runs, legal_balls, ball_number, current_batters, batters_yet, over_ended_early

def play_innings(batting_team, bowling_team, max_overs, max_bowler_overs):
    innings = Innings(batting_team, bowling_team)
    print(f"Players available to open the batting:")
    for idx, num in enumerate(batting_team.order, 1):
        print(f"{idx}: {num} {get_display_name(batting_team, num)}")
    openers = select_openers(batting_team)
    striker, non_striker = batting_team.players[openers[0]], batting_team.players[openers[1]]
    current_batters = [striker, non_striker]
    batters_yet = [num for num in batting_team.order if num not in batting_team.order[:2]]
    bowler_overs = {}
    wickets = 0
    over = 0
    prev_bowler = None
    while over < max_overs and wickets < 10:
        bowler_num = select_bowler(bowling_team, over, prev_bowler, bowler_overs)
        bowler = bowling_team.players[bowler_num]
        balls_this_over = 0
        over_runs = 0
        over_dots = 0
        legal_balls = 0
        ball_num = 1
        over_ended_early = False
        bowler_overs.setdefault(bowler_num, [])
        while legal_balls < 6:
            if wickets == 10 or current_batters[0] is None or current_batters[1] is None:
                over_ended_early = True
                break
            result = input_ball(current_batters, bowler, over, ball_num, bowling_team)
            if len(result) == 4:
                runs, event_type, fielders, swapped = result
            else:
                runs, event_type, fielders = result
                swapped = False
            if event_type == "end":
                over_ended_early = True
                break
            batter = current_batters[0]
            event = BallEvent(over, ball_num, bowler, batter, runs, event_type, fielders)
            innings.add_ball(event)
            batter.batted = True
            bowler.bowled = True
            wickets, over_runs, legal_balls, ball_num, current_batters, batters_yet, over_ended_early = process_ball_event(
                event_type, runs, fielders, swapped, innings, bowler, batter,
                current_batters, wickets, over, ball_num, batting_team, over_runs,
                legal_balls, ball_num, batters_yet
            )
            if over_ended_early:
                break
        if over_ended_early:
            print("OVER ENDED EARLY (all out, no batters, or innings ended).")
        else:
            print("OVER FINISHED.")
        bowler_overs[bowler_num].append(over)
        if over_runs == 0:
            bowler.bowling['maidens'] += 1
        prev_bowler = bowler_num
        over += 1
        if over > 0 and current_batters[0] and current_batters[1]:
            current_batters.reverse()
    print_batting_scorecard(innings)
    print_bowling_scorecard(innings)
    return innings