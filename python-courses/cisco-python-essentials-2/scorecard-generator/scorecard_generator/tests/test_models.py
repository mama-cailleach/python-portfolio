import unittest
from scorecard_generator.models import Player, Team

class TestPlayer(unittest.TestCase):
    def setUp(self):
        """This runs before each test method"""
        self.player = Player(number="7", name="Test Player")

    def test_player_initialization(self):
        """Test that a player is created with correct initial values"""
        self.assertEqual(self.player.number, "7")
        self.assertEqual(self.player.name, "Test Player")
        self.assertEqual(self.player.batting['runs'], 0)
        self.assertEqual(self.player.batting['balls'], 0)
        self.assertEqual(self.player.batting['dismissal'], 'not out')

    def test_player_str_representation(self):
        """Test the string representation of a player"""
        self.assertEqual(str(self.player), "7 Test Player")

class TestTeam(unittest.TestCase):
    def setUp(self):
        """This runs before each test method"""
        self.team = Team("Test Team")
        self.player1 = Player("1", "Player One")
        self.player2 = Player("2", "Player Two")

    def test_team_initialization(self):
        """Test that a team is created with correct initial values"""
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(len(self.team.players), 0)
        self.assertEqual(len(self.team.order), 0)

    def test_add_player(self):
        """Test adding players to a team"""
        self.team.add_player(self.player1)
        self.team.add_player(self.player2)
        
        self.assertEqual(len(self.team.players), 2)
        self.assertEqual(self.team.get_player("1").name, "Player One")
        self.assertEqual(self.team.get_player("2").name, "Player Two")

if __name__ == '__main__':
    unittest.main()
