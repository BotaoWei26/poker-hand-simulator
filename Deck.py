from Card import *
import random


class Deck:
    def __init__(self):
        self.cards = [Card(suit, number) for suit in ['c', 'd', 's', 'h'] for number in range(1, 14)]
        self.shuffle()

    def pretty_print(self):
        pp = []
        for card in self.cards:
            pp.append(card.pretty_print())
        return pp

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
