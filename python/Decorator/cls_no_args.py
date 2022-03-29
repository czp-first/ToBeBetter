# -*- coding: UTF-8 -*-
"""
@Summary : 不带参数的类装饰器
@Author  : Rey
@Time    : 2022-03-29 18:25:38
"""
from typing import Any

class Decorator(object):
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print(f'begin: {self.func.__name__}')
        result = self.func(*args, **kwargs)
        print(f'  end: {self.func.__name__}')
        return result
        

@Decorator
def say(name):
    print(name)


if __name__ == '__main__':
    say('huanhuan')
