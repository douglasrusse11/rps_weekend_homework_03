from models.player import Player
from models.game import Game

def run_game(hand1, hand2):
    player1 = Player("Player 1", hand1)
    player2 = Player("Player 2", hand2)
    game = Game(player1, player2)
    return game.play(), game.list_players()

