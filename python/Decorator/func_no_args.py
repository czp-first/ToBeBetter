# -*- coding: UTF-8 -*-
"""
@Summary : 普通的装饰器
@Author  : Rey
@Time    : 2022-03-29 18:12:55
"""

def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'begin: {func.__name__}')
        result = func(*args, **kwargs)
        print(f'  end: {func.__name__}')
        return result
    return wrapper


@decorator
def say(name):
    print(name)


if __name__ == '__main__':
    say('huanhuan')
