import unittest
from models.run_game import run_game

class TestRun_Game(unittest.TestCase):

    def test_run_game_rock_rock_returns_None(self):
        self.assertEqual(None, run_game("rock", "rock"))
    
    def test_run_game_paper_paper_returns_None(self):
        self.assertEqual(None, run_game("paper", "paper"))
    
    def test_run_game_scissors_scissors_returns_None(self):
        self.assertEqual(None, run_game("scissors", "scissors"))
    
    def test_run_game_rock_paper_returns_player2(self):
        winner = run_game("rock", "paper")
        self.assertEqual("Player 2", winner.name)
        self.assertEqual("paper", winner.hand)
    
    def test_run_game_paper_rock_returns_player1(self):
        winner = run_game("paper", "rock")
        self.assertEqual("Player 1", winner.name)
        self.assertEqual("paper", winner.hand)

    def test_run_game_paper_scissors_returns_player2(self):
        winner = run_game("paper", "scissors")
        self.assertEqual("Player 2", winner.name)
        self.assertEqual("scissors", winner.hand)

    def test_run_game_scissors_paper_returns_player1(self):
        winner = run_game("scissors", "paper")
        self.assertEqual("Player 1", winner.name)
        self.assertEqual("scissors", winner.hand)

    def test_run_game_scissors_rock_returns_player2(self):
        winner = run_game("scissors", "rock")
        self.assertEqual("Player 2", winner.name)
        self.assertEqual("rock", winner.hand)

    def test_run_game_rock_scissors_returns_player1(self):
        winner = run_game("rock", "scissors")
        self.assertEqual("Player 1", winner.name)
        self.assertEqual("rock", winner.hand)