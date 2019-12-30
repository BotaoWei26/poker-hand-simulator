from Deck import *
from Player import *
from hands import *
from copy import copy


class Poker:
    def __init__(self, players):
        self.deck = Deck()
        self.table = []
        self.players = [Player(p+1) for p in range(players)]

    def pretty_print(self):
        print("Table: ", end='')
        for card in self.table:
            card.pretty_print()
        print()
        for player in self.players:
            print("Player {}:".format(str(player.player_number)), end='')
            player.pretty_print()
            print()
        print()

    def deal_players(self):
        for player in self.players:
            player.deal(self.deck.draw())
            player.deal(self.deck.draw())

    def deal_table(self, times):
        for time in range(times):
            self.table.append(self.deck.draw())

    def play_round(self, round_num):
        if round_num == 1:
            self.deal_table(3)
        if round_num == 2:
            self.deal_table(1)
        if round_num == 3:
            self.deal_table(1)

    def winner(self):
        hands = []
        for player in self.players:
            cards = copy(player.cards)
            cards.extend(self.table)
            if len(cards) < 5:
                return []
            th = hand_type(cards)
            hands.append(th)
        top_hand = top(hands)

        winners = []
        for i in range(len(hands)):
            if top_hand == hands[i]:
                winners.append(i)
        return winners


