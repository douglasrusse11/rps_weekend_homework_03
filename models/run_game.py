from models.player import Player
from models.game import Game

def run_game(input1, input2, computer=False):
    if computer:
        player1 = Player(input1, input2)
        game = Game(player1)
        return game.play_computer(), game.list_players()
    else:
        player1 = Player("Player 1", input1)
        player2 = Player("Player 2", input2)
        game = Game(player1, player2)
        return game.play(), game.list_players()

