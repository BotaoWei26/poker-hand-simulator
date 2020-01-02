from Poker import *

p = Poker(3)


p.pretty_print()
input()
for i in p.odds_generator():
    print(i)


p.deal_players()
p.play_round(1)
p.play_round(2)

p.pretty_print()
input()
for i in p.odds_generator():
    print(i)


p.play_round(3)

p.pretty_print()
input()
for i in p.odds_generator():
    print(i)
