# -*- coding: UTF-8 -*-
"""
@Summary : 带参数的类装饰器
@Author  : Rey
@Time    : 2022-03-29 18:29:13
"""


class ShowLove(object):
    def __init__(self, language) -> None:
        self.language = language

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.language == 'chinese':
                print('我爱你')
            elif self.language == 'english':
                print('i love u')
            else:
                print('unknown')
            return func(*args, **kwargs)
        return wrapper


@ShowLove('english')
def huanhuan():
    print('huanhuan')


if __name__ == '__main__':
    huanhuan()
