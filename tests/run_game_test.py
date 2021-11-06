import unittest
from models.run_game import run_game

class TestRun_Game(unittest.TestCase):

    def test_run_game_rock_rock_returns_None(self):
        winner, players = run_game("rock", "rock")
        self.assertEqual(None, winner)
    
    def test_run_game_paper_paper_returns_None(self):
        winner, players = run_game("paper", "paper")
        self.assertEqual(None, winner)
    
    def test_run_game_scissors_scissors_returns_None(self):
        winner, players = run_game("scissors", "scissors")
        self.assertEqual(None, winner)
    
    def test_run_game_rock_paper_returns_player2(self):
        winner, players = run_game("rock", "paper")
        self.assertEqual("Player 2", winner.name)
        self.assertEqual("paper", winner.hand)
    
    def test_run_game_paper_rock_returns_player1(self):
        winner, players = run_game("paper", "rock")
        self.assertEqual("Player 1", winner.name)
        self.assertEqual("paper", winner.hand)

    def test_run_game_paper_scissors_returns_player2(self):
        winner, players = run_game("paper", "scissors")
        self.assertEqual("Player 2", winner.name)
        self.assertEqual("scissors", winner.hand)

    def test_run_game_scissors_paper_returns_player1(self):
        winner, players = run_game("scissors", "paper")
        self.assertEqual("Player 1", winner.name)
        self.assertEqual("scissors", winner.hand)

    def test_run_game_scissors_rock_returns_player2(self):
        winner, players = run_game("scissors", "rock")
        self.assertEqual("Player 2", winner.name)
        self.assertEqual("rock", winner.hand)

    def test_run_game_rock_scissors_returns_player1(self):
        winner, players = run_game("rock", "scissors")
        self.assertEqual("Player 1", winner.name)
        self.assertEqual("rock", winner.hand)

    def test_run_game_rock_banana_returns_404(self):
        winner, players = run_game("rock", "banana")
        self.assertEqual(404, winner)

    def test_run_game_dinosaur_paper_returns_404(self):
        winner, players = run_game("dinosaur", "paper")
        self.assertEqual(404, winner)