# -*- coding: UTF-8 -*-
"""
@Summary : 选择排序
@Author  : Rey
@Time    : 2021-01-13 08:51
"""


def selection_sort(origin):

    for i in range(len(origin)-1, 0, -1):

        max_index = 0
        for j in range(1, i+1):
            if origin[j] > origin[max_index]:
                max_index = j

        origin[i], origin[max_index] = origin[max_index], origin[i]

    return origin


if __name__ == '__main__':
    a = [1, 5, 3, 9, 22]
    print(selection_sort(a))
