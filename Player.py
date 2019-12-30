from Card import *


class Player:
    def __init__(self, p):
        self.player_number = p
        self.cards = []

    def deal(self, card):
        self.cards.append(card)

    def pretty_print(self):
        pp = []
        for card in self.cards:
            pp.append(card.pretty_print())
        return pp
