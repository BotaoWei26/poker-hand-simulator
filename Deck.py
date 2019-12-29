from Card import *
import random


class Deck:
    def __init__(self):
        self.cards = [Card(suit, number) for suit in ['c', 'd', 's', 'h'] for number in range(1, 14)]
        self.shuffle()

    def pretty_print(self):
        for card in self.cards:
            card.pretty_print()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
