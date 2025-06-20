import unittest
from io import StringIO
from unittest.mock import patch
from scorecard_generator.models import Player, Team, Innings, BallEvent
from scorecard_generator.scorecard import print_batting_scorecard, print_bowling_scorecard

class TestScorecardGeneration(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test"""
        # Create teams
        self.batting_team = Team("Test Batting Team")
        self.bowling_team = Team("Test Bowling Team")
        
        # Create batters
        self.opener1 = Player("1", "Test Opener One")
        self.opener2 = Player("2", "Test Opener Two")
        self.batter3 = Player("3", "Test Batter Three")
        
        # Mark openers as having batted
        self.opener1.batted = True
        self.opener2.batted = True
        
        # Create bowlers
        self.bowler1 = Player("11", "Test Bowler One")
        self.bowler2 = Player("12", "Test Bowler Two")
        
        # Add players to teams
        self.batting_team.add_player(self.opener1)
        self.batting_team.add_player(self.opener2)
        self.batting_team.add_player(self.batter3)
        self.bowling_team.add_player(self.bowler1)
        self.bowling_team.add_player(self.bowler2)
        
        # Set batting order
        self.batting_team.order = ["1", "2", "3"]
        
        # Set up innings
        self.innings = Innings(self.batting_team, self.bowling_team)
        
        # Add some sample events
        # First over - 6 runs (1, 4, dot, dot, 1, dot)
        self.add_over_events(0, self.bowler1, [
            (self.opener1, 1, "normal", []),
            (self.opener2, 4, "normal", []),
            (self.opener2, 0, "normal", []),
            (self.opener2, 0, "normal", []),
            (self.opener2, 1, "normal", []),
            (self.opener1, 0, "normal", [])
        ])
        
        # Second over - 8 runs (wide, 2, 4, dot, 1, dot, dot)
        self.add_over_events(1, self.bowler2, [
            (self.opener1, 1, "wide", []),
            (self.opener1, 2, "normal", []),
            (self.opener1, 4, "normal", []),
            (self.opener1, 0, "normal", []),
            (self.opener1, 1, "normal", []),
            (self.opener2, 0, "normal", [])
        ])

    def add_over_events(self, over, bowler, balls):
        """Helper method to add a series of ball events to the innings"""
        for ball_num, (batter, runs, event_type, fielders) in enumerate(balls, 1):
            event = BallEvent(over, ball_num, bowler, batter, runs, event_type, fielders)
            self.innings.add_ball(event)
            
            # Update statistics based on event type
            if event_type == "normal":
                batter.batting['runs'] += runs
                batter.batting['balls'] += 1
                if runs == 4:
                    batter.batting['4s'] += 1
                elif runs == 6:
                    batter.batting['6s'] += 1
                    
                bowler.bowling['runs'] += runs
                bowler.bowling['balls'] += 1
                if runs == 0:
                    bowler.bowling['dots'] += 1
            elif event_type == "wide":
                self.innings.extras['wides'] += runs
                bowler.bowling['wides'] += runs
                bowler.bowling['runs'] += runs

    def test_batting_scorecard(self):
        """Test batting scorecard generation"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print_batting_scorecard(self.innings)
            output = fake_output.getvalue()
            
            # Check headers are present
            self.assertIn("Batting: Test Batting Team", output)
            self.assertIn("Player Name", output)
            self.assertIn("Dismissal", output)
            self.assertIn("Runs", output)
            self.assertIn("Balls", output)
            self.assertIn("SR", output)
            
            # Check batter stats
            self.assertIn("Test Opener One", output)  # Name should be in the output somewhere
            self.assertIn("8", output)  # Runs
            self.assertIn("4", output)  # Balls
            
            # Check extras are shown
            self.assertIn("Extras", output)
            self.assertIn("(w 1)", output)  # 1 wide

    def test_bowling_scorecard(self):
        """Test bowling scorecard generation"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print_bowling_scorecard(self.innings)
            output = fake_output.getvalue()
            
            # Check headers are present
            self.assertIn("Bowler", output)
            self.assertIn("Overs", output)
            self.assertIn("M", output)
            self.assertIn("Runs", output)
            self.assertIn("Wkts", output)
            self.assertIn("Econ", output)
            
            # Check bowler stats
            self.assertIn("Test Bowler One", output)
            self.assertIn("1.0", output)  # Overs
            self.assertIn("6", output)  # Runs
            self.assertIn("0", output)  # Wickets
            
            self.assertIn("Test Bowler Two", output)
            self.assertIn("0.5", output)  # Overs (5 balls bowled)
            self.assertIn("8", output)  # Runs (7 + 1 wide)

    def test_batting_extras_display(self):
        """Test that extras are properly displayed in the batting scorecard"""
        # Add some extras
        self.innings.extras['byes'] = 2
        self.innings.extras['leg byes'] = 1
        self.innings.extras['wides'] = 1
        self.innings.extras['no balls'] = 1
        
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print_batting_scorecard(self.innings)
            output = fake_output.getvalue()
            
            self.assertIn("Extras", output)
            self.assertIn("b 2", output)
            self.assertIn("lb 1", output)
            self.assertIn("w 1", output)
            self.assertIn("nb 1", output)
            self.assertIn("5", output)  # Total extras

if __name__ == '__main__':
    unittest.main()

