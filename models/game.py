class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.HANDS = {"rock": 0, "paper": 1, "scissors": 2}

    def play(self):
        if self.player1.hand == self.player2.hand:
            return None
        else:
            return self.player2