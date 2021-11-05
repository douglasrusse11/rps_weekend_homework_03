import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Bob", "rock")
        self.player2 = Player("Tom", "paper")

    def test_game_has_player1(self):
        self.game = Game(self.player1, self.player2)
        self.assertEqual(self.player1, self.game.player1)

    @unittest.skip('')
    def test_game_has_player2(self):
        self.game = Game(self.player1, self.player2)
        self.assertEqual(self.player2, self.game.player2)

    @unittest.skip('')
    def test_game_has_HANDS(self):
        self.game = Game(self.player1, self.player2)
        self.assertEqual({"rock": 0, "paper": 1, "scissors": 2}, self.game.HANDS)