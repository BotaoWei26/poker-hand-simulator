class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def pretty_print(self):
        return str(self.number) + str(self.suit)
