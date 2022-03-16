# -*- coding: UTF-8 -*-
"""
@Summary : 
@Author  : Rey
@Time    : 2021-01-13 08:33
@Log     :
           author datetime(DESC) summary
           Rey  2021-01-13 08:33  init
"""
from __future__ import absolute_import


def bubble_sort(origin):
    """
    n^2
    :param origin:
    :return:
    """
    for i in range(len(origin)-1, 0, -1):

        for j in range(i):

            if origin[j] > origin[j+1]:
                origin[j], origin[j+1] = origin[j+1], origin[j]

    return origin


if __name__ == '__main__':
    a = [1, 5, 3, 9, 22]
    print(bubble_sort(a))
