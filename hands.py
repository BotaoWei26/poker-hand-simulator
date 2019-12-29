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
    flush = check_flush(cards)
    straight = check_straight(cards)
    alike = find_alike(cards)

    if len(flush) != 0 and straight != 0:
        return [hand_ranks["straight_flush"], straight, 0, 0, 0, 0]
    elif alike[0][1] == 4:
        return [hand_ranks["quad"], alike[0][0], max(alike[1:], key=lambda x: x[0])[0], 0, 0, 0]
    elif alike[0][1] == 3 and alike[1][1] >= 2:
        return [hand_ranks["full_house"], alike[0][0], alike[1][0], 0, 0, 0]
    elif len(flush) != 0:
        return [hand_ranks["flush"], flush[0], flush[1], flush[2], flush[3], flush[4]]
    elif straight != 0:
        return [hand_ranks["straight"], straight, 0, 0, 0, 0]
    elif alike[0][1] == 3:
        return [hand_ranks["trips"], alike[0][0], alike[1][0], alike[2][0], 0, 0]
    elif alike[0][1] == 2 and alike[1][1] == 2:
        return [hand_ranks["two_pair"], alike[0][0], alike[1][0], alike[2][0], 0, 0]
    elif alike[0][1] == 2:
        return [hand_ranks["pair"], alike[0][0], alike[1][0], alike[2][0], alike[3][0], 0]
    else:
        return [hand_ranks["high_card"], alike[0][0], alike[1][0], alike[2][0], alike[3][0], alike[4][0]]


def sorted_numbers(cards):
    numbers = []
    for card in cards:
        numbers.append(card.number)
    numbers.sort(reverse=True)
    return numbers


def ace_high(numbers):
    return [i if i != 1 else 14 for i in numbers]


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
        return sorted(c)[0:5]
    if len(d) >= 5:
        return sorted(d)[0:5]
    if len(s) >= 5:
        return sorted(s)[0:5]
    if len(h) >= 5:
        return sorted(h)[0:5]
    return []


def check_straight(cards):
    numbers = sorted_numbers(cards)
    if 1 in numbers:
        numbers.append(14)
    count = 1
    top = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i - 1] - numbers[i] == 1:
            count += 1
        else:
            count = 1
            top = numbers[i]
        if count == 5:
            return top
    return 0


def find_alike(cards):
    numbers = sorted_numbers(ace_high(cards))

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

