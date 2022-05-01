# -*- coding: UTF-8 -*-
"""
@Summary : example1 of template
@Author  : Rey
@Time    : 2022-05-01 19:47:40
"""

from cowpy import cow


def dots_style(msg: str):
    msg = msg.capitalize()
    msg = '.' * 10 + msg + '.' * 10
    return msg


def admire_style(msg: str):
    msg = msg.upper()
    return '!'.join(msg)


def cow_style(msg):
    msg = cow.milk_random_cow(msg)
    return msg


def generate_banner(msg, style=dots_style):
    print('-- start of banner --')
    print(style(msg))
    print('-- end of banner --\n\n')


def main():
    msg = 'happy coding'
    [generate_banner(msg, style) for style in (dots_style, admire_style, cow_style)]


if __name__ == '__main__':
    main()
