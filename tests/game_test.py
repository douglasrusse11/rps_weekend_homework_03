import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Bob", "rock")
        self.player2 = Player("Tom", "paper")
        self.player3 = Player("Abe", "scissors")
        self.player4 = Player("Rex", "microscope")

    def test_game_has_player1(self):
        self.game = Game(self.player1, self.player2)
        self.assertEqual(self.player1, self.game.player1)

    def test_game_has_player2(self):
        self.game = Game(self.player1, self.player2)
        self.assertEqual(self.player2, self.game.player2)

    def test_game_has_HANDS(self):
        self.game = Game(self.player1, self.player2)
        self.assertEqual({"rock": 0, "paper": 1, "scissors": 2}, self.game.HANDS)

    def test_play_same_hands_returns_None(self):
        self.game = Game(self.player1, self.player1)
        self.assertEqual(None, self.game.play())

    def test_play_player1_player2_returns_player2(self):
        self.game = Game(self.player1, self.player2)
        self.assertEqual(self.player2, self.game.play())
    
    def test_play_player2_player1_returns_player2(self):
        self.game = Game(self.player2, self.player1)
        self.assertEqual(self.player2, self.game.play())
    
    def test_play_player2_player3_returns_player3(self):
        self.game = Game(self.player2, self.player3)
        self.assertEqual(self.player3, self.game.play())
    
    def test_play_player3_player2_returns_player3(self):
        self.game = Game(self.player3, self.player2)
        self.assertEqual(self.player3, self.game.play())
    
    def test_play_player1_player3_returns_player1(self):
        self.game = Game(self.player1, self.player3)
        self.assertEqual(self.player1, self.game.play())
    
    def test_play_player3_player1_returns_player1(self):
        self.game = Game(self.player3, self.player1)
        self.assertEqual(self.player1, self.game.play())
    
    @unittest.skip('')
    def test_play_player1_player4_returns_404(self):
        self.game = Game(self.player1, self.player4)
        self.assertEqual(404, self.game.play())
    
    @unittest.skip('')
    def test_play_player4_player1_returns_404(self):
        self.game = Game(self.player4, self.player1)
        self.assertEqual(404, self.game.play())