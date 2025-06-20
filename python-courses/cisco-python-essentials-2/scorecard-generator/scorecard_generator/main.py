from .team_utils import choose_team_xi
from .game_logic import play_innings
from .models import MAX_OVERS, MAX_BOWLER_OVERS

### just to not forget this info
# cd /workspaces/python-portfolio/python-courses/cisco-python-essentials-2/scorecard-generator
# python -m scorecard_generator.main
###

def main():
    print("Cricket T20 Scorecard Creator/Analyzer\n")
    ready = input("Do you have your starting XIs ready? (y/n): ").strip().lower()
    if ready != "y":
        print("Please use the team manager (team_utils.py) to create/select your teams and starting XIs before running the scorecard generator.")
        return

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

    print(f"\nFirst Innings: {batting_first.name} Batting")
    innings1 = play_innings(batting_first, bowling_first, MAX_OVERS, MAX_BOWLER_OVERS)

    print(f"\nSecond Innings: {bowling_first.name} Batting")
    innings2 = play_innings(bowling_first, batting_first, MAX_OVERS, MAX_BOWLER_OVERS)

    # You may wish to add a basic winner logic here
    score1, wickets1, overs1, rr1 = innings1.get_score()
    score2, wickets2, overs2, rr2 = innings2.get_score()
    print("\nRESULT:")
    if score1 > score2:
        print(f"{batting_first.name} win by {score1 - score2} runs!")
    elif score2 > score1:
        wickets_left = 10 - wickets2
        print(f"{bowling_first.name} win by {wickets_left} wicket(s)!")
    else:
        print("Match tied!")

if __name__ == "__main__":
    main()