class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.HANDS = {"rock": 0, "paper": 1, "scissors": 2}

    def play(self):
        if self.invalid_hand():
            return 404
        if self.player1.hand == self.player2.hand:
            return None
        elif self.hand(self.player1) == 0 and self.hand(self.player2) == 2:
            return self.player1
        elif self.hand(self.player2) == 0 and self.hand(self.player1) == 2:
            return self.player2
        elif self.hand(self.player1) < self.hand(self.player2):
            return self.player2
        else:
            return self.player1

    def hand(self, player):
        return self.HANDS[player.hand]

    
    def invalid_hand(self):
        return not self.player1.hand in self.HANDS or not self.player2.hand in self.HANDS