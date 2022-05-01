# -*- coding: UTF-8 -*-
"""
@Summary : example2 of strategy
@Author  : Rey
@Time    : 2022-05-01 19:05:59
"""

import time

SLOW = 3
LIMIT = 5
WARNING = 'to bad, you picked the slow algorithm :('


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i+1) % n]


def all_unique_sort(s):
    if len(s) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    srt_str = sorted(s)
    for (c1, c2) in pairs(srt_str):
        if c1 == c2:
            return False
    return True


def all_unique_set(s):
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    return True if len(set(s)) == len(s) else False


def all_unique(s, strategy):
    return strategy(s)


def main():
    while True:
        word = None
        while not word:
            word = input('Insert word (type quit to exit)>')
            if word == 'quit':
                print('bye')
                return

            strategy_picked = None
            strategies = {'1': all_unique_set, '2': all_unique_sort}
            while strategy_picked not in strategies:
                strategy_picked = input('Choose strategy: [1] Use a set, [2] Sort and pair>')
                try:
                    strategy = strategies[strategy_picked]
                    print(f'all_unique({word}): {all_unique(word, strategy)}')
                except KeyError:
                    print(f'Incorrect option: {strategy_picked}')
            print()


if __name__ == '__main__':
    main()
