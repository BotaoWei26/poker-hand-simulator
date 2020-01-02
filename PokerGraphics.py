from tkinter import *
from Poker import *


class PokerGraphics:
    def __init__(self, window, num_players):
        self.window = window
        self.num_players = num_players
        self.poker = Poker(num_players)

        self.card_sprites = {
            "1c": PhotoImage(file="sprites/1c.gif"),
            "1d": PhotoImage(file="sprites/1d.gif"),
            "1h": PhotoImage(file="sprites/1h.gif"),
            "1s": PhotoImage(file="sprites/1s.gif"),
            "2c": PhotoImage(file="sprites/2c.gif"),
            "2d": PhotoImage(file="sprites/2d.gif"),
            "2h": PhotoImage(file="sprites/2h.gif"),
            "2s": PhotoImage(file="sprites/2s.gif"),
            "3c": PhotoImage(file="sprites/3c.gif"),
            "3d": PhotoImage(file="sprites/3d.gif"),
            "3h": PhotoImage(file="sprites/3h.gif"),
            "3s": PhotoImage(file="sprites/3s.gif"),
            "4c": PhotoImage(file="sprites/4c.gif"),
            "4d": PhotoImage(file="sprites/4d.gif"),
            "4h": PhotoImage(file="sprites/4h.gif"),
            "4s": PhotoImage(file="sprites/4s.gif"),
            "5c": PhotoImage(file="sprites/5c.gif"),
            "5d": PhotoImage(file="sprites/5d.gif"),
            "5h": PhotoImage(file="sprites/5h.gif"),
            "5s": PhotoImage(file="sprites/5s.gif"),
            "6c": PhotoImage(file="sprites/6c.gif"),
            "6d": PhotoImage(file="sprites/6d.gif"),
            "6h": PhotoImage(file="sprites/6h.gif"),
            "6s": PhotoImage(file="sprites/6s.gif"),
            "7c": PhotoImage(file="sprites/7c.gif"),
            "7d": PhotoImage(file="sprites/7d.gif"),
            "7h": PhotoImage(file="sprites/7h.gif"),
            "7s": PhotoImage(file="sprites/7s.gif"),
            "8c": PhotoImage(file="sprites/8c.gif"),
            "8d": PhotoImage(file="sprites/8d.gif"),
            "8h": PhotoImage(file="sprites/8h.gif"),
            "8s": PhotoImage(file="sprites/8s.gif"),
            "9c": PhotoImage(file="sprites/9c.gif"),
            "9d": PhotoImage(file="sprites/9d.gif"),
            "9h": PhotoImage(file="sprites/9h.gif"),
            "9s": PhotoImage(file="sprites/9s.gif"),
            "10c": PhotoImage(file="sprites/10c.gif"),
            "10d": PhotoImage(file="sprites/10d.gif"),
            "10h": PhotoImage(file="sprites/10h.gif"),
            "10s": PhotoImage(file="sprites/10s.gif"),
            "11c": PhotoImage(file="sprites/11c.gif"),
            "11d": PhotoImage(file="sprites/11d.gif"),
            "11h": PhotoImage(file="sprites/11h.gif"),
            "11s": PhotoImage(file="sprites/11s.gif"),
            "12c": PhotoImage(file="sprites/12c.gif"),
            "12d": PhotoImage(file="sprites/12d.gif"),
            "12h": PhotoImage(file="sprites/12h.gif"),
            "12s": PhotoImage(file="sprites/12s.gif"),
            "13c": PhotoImage(file="sprites/13c.gif"),
            "13d": PhotoImage(file="sprites/13d.gif"),
            "13h": PhotoImage(file="sprites/13h.gif"),
            "13s": PhotoImage(file="sprites/13s.gif"),
            "back": PhotoImage(file="sprites/back.gif")
        }

        window.title("Poker")
        window.geometry("1200x800")

        self.table_label = Label(self.window, text="TABLE:")
        self.table_label.grid(column=0, row=0)
        self.table_cards = []

        self.table_cards = []
        for i in range(5):
            self.table_cards.append(Label(self.window, image=self.card_sprites["back"], height=75, width=50, bg='black'))
            self.table_cards[i].grid(column=i+1, row=0)

        self.player_labels = []
        self.player_cards = []
        for i in range(self.num_players):
            self.player_labels.append(Label(self.window, text="PLAYER {}:".format(i)))
            self.player_labels[i].grid(column=0, row=i+1)
            cards = []
            for j in range(2):
                cards.append(Label(self.window, image=self.card_sprites["back"], height=75, width=50, bg='black'))
                cards[j].grid(column=j+1, row=i+1)
            self.player_cards.append(cards)

        self.deal_button = Button(window, text="DRAW", command=self.deal)
        self.deal_button.grid(column=8, row=num_players+1)
        self.count = 0

        self.restart_button = Button(window, text="RESTART", command=self.restart)
        self.restart_button.grid(column=8, row=num_players+2)

        self.odds_labels = []
        for i in range(self.num_players):
            self.odds_labels.append([Label(self.window, text="Winning: 0.00%"), Label(self.window, text="Split: 0.00%")])
            self.odds_labels[i][0].grid(column=4, row=i+1)
            self.odds_labels[i][1].grid(column=5, row=i+1)

    def draw_cards(self):
        for i in range(5):
            if i < len(self.poker.table):
                card_pp = self.poker.table[i].pretty_print()
            else:
                card_pp = "back"
            self.table_cards[i].config(image=self.card_sprites[card_pp])

        for i in range(self.num_players):
            for j in range(2):
                if j < len(self.poker.players[i].cards):
                    card_pp = self.poker.players[i].pretty_print()[j]
                else:
                    card_pp = "back"
                self.player_cards[i][j].config(image=self.card_sprites[card_pp])


    def deal(self):
        if self.count == 0:
            self.poker.deal_players()
        elif self.count == 1:
            self.poker.play_round(1)
        elif self.count == 2:
            self.poker.play_round(2)
        elif self.count == 3:
            self.poker.play_round(3)
        else:
            return
        self.count += 1
        self.draw_cards()
        self.odds = self.poker.odds_generator()
        self.draw_odds()

    def draw_odds(self):
        try:
            odds = next(self.odds)
        except StopIteration:
            return
        for i in range(self.num_players):
            self.odds_labels[i][0].config(text="Winning: {0:.2%}".format(odds[i][0]))
            self.odds_labels[i][1].config(text="Split: {0:.2%}".format(odds[i][1]))
        self.window.after_idle(func=self.draw_odds)

    def restart(self):
        self.count = 0
        self.poker = Poker(self.num_players)
        self.draw_cards()
