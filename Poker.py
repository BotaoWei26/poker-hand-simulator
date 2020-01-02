from Deck import *
from Player import *
from hands import *
from copy import copy
from itertools import combinations


class Poker:
    def __init__(self, players):
        self.deck = Deck()
        self.table = []
        self.players = [Player(p+1) for p in range(players)]

    def pretty_print(self):
        print("Table: ", end='')
        for card in self.table:
            print(card.pretty_print(), end=' ')
        print()
        for player in self.players:
            print("Player {}:".format(str(player.player_number)), end='')
            print(player.pretty_print())
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

    def odds_generator(self):
        odds = [[0, 0] for p in range(len(self.players))]
        odds_tries = 0
        odds_deck = copy(self.deck)
        odds_deck.shuffle()
        test_cards = combinations(odds_deck.cards, 5 - len(self.table))

        for test_cards_pick in test_cards:
            hands = []
            for player in self.players:
                cards = copy(player.cards)
                cards.extend(self.table)
                cards.extend(test_cards_pick)
                th = hand_type(cards)
                hands.append(th)
            top_hand = top(hands)

            for i in range(len(hands)):
                if top_hand == hands[i]:
                    if len(list(filter(lambda x: x == top_hand, hands))) == 1:
                        odds[i][0] += 1
                    else:
                        odds[i][1] += 1
            odds_tries += 1
            yield list(map(lambda x: [x[0] / odds_tries, x[1] / odds_tries], odds))
        return

