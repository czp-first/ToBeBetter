# -*- coding: UTF-8 -*-
"""
@Summary : decorator
@Author  : Rey
@Time    : 2022-03-29 14:53:48
"""
import functools
import inspect


def is_admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 获取函数执行时的参数, 不必检查参数 username 是基于位置的参数还是关键字参数
        func_args = inspect.getcallargs(func, *args, **kwargs)
        if func_args.get('username') != 'admin':
            raise Exception('permission denied!')
        return func(*args, **kwargs)
    return wrapper
