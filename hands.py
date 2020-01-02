from Card import *
from functools import reduce

hand_ranks = {
    "straight_flush": 9,
    "quad": 8,
    "full_house": 7,
    "flush": 6,
    "straight": 5,
    "trips": 4,
    "two_pair": 3,
    "pair": 2,
    "high_card": 1
}


def hand_type(cards):
    straight_flush = check_straight_flush(cards)
    flush = check_flush(cards)
    straight = check_straight(cards)
    alike = find_alike(cards)
    number_rank = sorted(ace_high(set(map(lambda x: x.number, cards))), reverse=True)

    if straight_flush != 0:
        return [hand_ranks["straight_flush"], straight_flush, 0, 0, 0, 0]
    elif alike[0][1] == 4:
        number_rank.remove(alike[0][0])
        return [hand_ranks["quad"], alike[0][0], number_rank[0], 0, 0, 0]
    elif alike[0][1] == 3 and alike[1][1] >= 2:
        return [hand_ranks["full_house"], alike[0][0], alike[1][0], 0, 0]
    elif len(flush) != 0:
        return [hand_ranks["flush"], flush[0], flush[1], flush[2], flush[3], flush[4]]
    elif straight != 0:
        return [hand_ranks["straight"], straight, 0, 0, 0, 0]
    elif alike[0][1] == 3:
        number_rank.remove(alike[0][0])
        return [hand_ranks["trips"], alike[0][0], number_rank[0], number_rank[1], 0, 0]
    elif alike[0][1] == 2 and alike[1][1] == 2:
        number_rank.remove(alike[0][0])
        number_rank.remove(alike[1][0])
        return [hand_ranks["two_pair"], alike[0][0], alike[1][0], number_rank[0], 0, 0]
    elif alike[0][1] == 2:
        number_rank.remove(alike[0][0])
        return [hand_ranks["pair"], alike[0][0], number_rank[0], number_rank[1], number_rank[2], 0]
    else:
        return [hand_ranks["high_card"], number_rank[0], number_rank[1], number_rank[2], number_rank[3], number_rank[4]]


def sorted_numbers(cards):
    numbers = []
    for card in cards:
        numbers.append(card.number)
    numbers.sort(reverse=True)
    return numbers


def ace_high(numbers):
    return [i if i != 1 else 14 for i in numbers]


def check_straight_flush(cards):
    flush = check_flush(cards)
    if len(flush) != 0:
        return check_straight(list(filter(lambda x: x.number in flush, cards)))
    return 0


def check_flush(cards):
    c = []
    d = []
    s = []
    h = []
    for card in cards:
        if card.suit == 'c':
            c.append(card.number)
        if card.suit == 'd':
            d.append(card.number)
        if card.suit == 's':
            s.append(card.number)
        if card.suit == 'h':
            h.append(card.number)
    if len(c) >= 5:
        return sorted(ace_high(c), reverse=True)
    if len(d) >= 5:
        return sorted(ace_high(d), reverse=True)
    if len(s) >= 5:
        return sorted(ace_high(s), reverse=True)
    if len(h) >= 5:
        return sorted(ace_high(h), reverse=True)
    return []


def check_straight(cards):
    numbers = sorted_numbers(cards)
    if 1 in numbers:
        numbers.insert(0, 14)
    count = 1
    top = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i - 1] - numbers[i] == 1:
            count += 1
        elif numbers[i - 1] - numbers[i] != 0:
            count = 1
            top = numbers[i]
        if count == 5:
            return top
    return 0


def find_alike(cards):
    numbers = sorted(ace_high(sorted_numbers(cards)), reverse=True)

    alike = []
    count = 1
    for i in range(1, len(numbers)):
        if numbers[i - 1] != numbers[i]:
            alike.append([numbers[i - 1], count])
            count = 1
        else:
            count += 1
    alike.append([numbers[-1], count])
    return sorted(alike, key=lambda x: x[1], reverse=True)


def top(hands):
    for i in range(5):
        hands = list(filter(lambda x: x[i] == max(hands, key=lambda y: y[i])[i], hands))
    return hands[0]