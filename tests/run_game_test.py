import unittest
from models.run_game import run_game
from models.player import Player

class TestRun_Game(unittest.TestCase):

    @unittest.skip('')
    def test_run_game_rock_rock_returns_None(self):
        self.assertEqual(None, run_game("rock", "rock"))
    
    @unittest.skip('')
    def test_run_game_paper_paper_returns_None(self):
        self.assertEqual(None, run_game("paper", "paper"))
    
    @unittest.skip('')
    def test_run_game_scissors_scissors_returns_None(self):
        self.assertEqual(None, run_game("scissors", "scissors"))
    
    @unittest.skip('')
    def test_run_game_rock_paper_returns_player2(self):
        self.assertEqual(Player("Player 2", "paper"), run_game("rock", "paper"))
    
    @unittest.skip('')
    def test_run_game_paper_rock_returns_player1(self):
        self.assertEqual(Player("Player 1", "paper"), run_game("paper", "rock"))
    
    @unittest.skip('')
    def test_run_game_paper_scissors_returns_player2(self):
        self.assertEqual(Player("Player 2", "scissors"), run_game("paper", "scissors"))
    
    @unittest.skip('')
    def test_run_game_scissors_paper_returns_player1(self):
        self.assertEqual(Player("Player 1", "scissors"), run_game("scissors", "paper"))
    
    @unittest.skip('')
    def test_run_game_scissors_rock_returns_player2(self):
        self.assertEqual(Player("Player 2", "rock"), run_game("scissors", "rock"))
    
    @unittest.skip('')
    def test_run_game_rock_scissors_returns_player1(self):
        self.assertEqual(Player("Player 1", "rock"), run_game("rock", "scissors"))