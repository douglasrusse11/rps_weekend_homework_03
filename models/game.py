class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.HANDS = {"rock": 0, "paper": 1, "scissors": 2}

    def play(self):
        if self.player1.hand == self.player2.hand:
            return None
        elif self.HANDS[self.player1.hand] == 0 and self.HANDS[self.player2.hand] == 2:
            return self.player1
        elif self.HANDS[self.player2.hand] == 0 and self.HANDS[self.player1.hand] == 2:
            return self.player2
        elif self.HANDS[self.player1.hand] < self.HANDS[self.player2.hand]:
            return self.player2
        else:
            return self.player1