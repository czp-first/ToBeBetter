# -*- coding: UTF-8 -*-
"""
@Summary : 二分查找, leecode: 704
@Author  : Rey
@Time    : 2022-03-19 22:06:36
"""

def binary_search(wait_list, target) -> int:
    """二分查找

    :param list wait_list: 待查列表
    :param _type_ target: 目标元素
    :return int: 目标位置
    """

    left = 0
    right = len(wait_list) - 1

    while left <= right:
        cur = (left + right) // 2
        if wait_list[cur] == target:
            return cur
        
        if wait_list[cur] < target:
            left = cur + 1
        else:
            right = cur - 1
    
    return -1
