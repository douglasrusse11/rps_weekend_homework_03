import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Bob", "rock")

    def test_player_has_name(self):
        self.assertEqual("Bob", self.player.name)

    def test_player_has_hand(self):
        self.assertEqual("rock", self.player.hand)