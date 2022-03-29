# -*- coding: UTF-8 -*-
"""
@Summary : 带参数的装饰器
@Author  : Rey
@Time    : 2022-03-29 18:17:49
"""

def show_love(language):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if language == 'chinese':
                print('我爱你')
            elif language == 'english':
                print('i love u')
            else:
                print('unknown')
            return func(*args, **kwargs)
        return wrapper
    return decorator


@show_love('english')
def huanhuan():
    print('huanhuan')


if __name__ == '__main__':
    huanhuan()
