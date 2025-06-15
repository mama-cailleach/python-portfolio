from collections import defaultdict

BALLS_PER_OVER = 6
MAX_OVERS = 2
MAX_BOWLER_OVERS = 1

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
        self.players = {}
        self.order = []
        self.bowler_order = []
        self.wicketkeeper_number = None
        self.captain_number = None

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
        self.bowler = bowler
        self.batter = batter
        self.runs = runs
        self.event = event
        self.fielders = fielders or []

class Innings:
    def __init__(self, batting_team, bowling_team):
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.balls = []
        self.current_batters = []
        self.dismissed = []
        self.did_not_bat = []
        self.fall_of_wickets = []
        self.extras = defaultdict(int)
        self.bowler_overs = defaultdict(list)

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