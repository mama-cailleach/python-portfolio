import random

batsman_name = "Virat Kohli"
bowler_name = "Pat Cummings"

print("Welcome To The One Over Simulation!\n")

print('Batsman: {}'.format(batsman_name))
print('versus')
print('Bowler: {}\n'.format(bowler_name))


batsman_one_total = 0
bowler_one_wicket = 0
over_one_total = 0

for ball in range(1, 7):
    what_happened = random.randint(0, 6)
    if (what_happened == 5):
        print("Ball {}.{}: {} to {}: OUT!".format(over_one_total, ball, bowler_name, batsman_name))
        bowler_one_wicket += 1
        #over_one_total += 1
        break
    else:
        batsman_one_total = batsman_one_total + what_happened
        print("Ball {}.{}: {} to {}: {} runs".format( over_one_total, ball, bowler_name, batsman_name, what_happened))
    if (ball == 6):
        over_one_total += 1


print("\nEnd of over {}: Batter: {} {}; Bowler: {} {}-{}".format(over_one_total, batsman_name, batsman_one_total, bowler_name, bowler_one_wicket, batsman_one_total))
