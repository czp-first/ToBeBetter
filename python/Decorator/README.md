
## 执行过程

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@decorator
def add(a, b):
    ...

add(1, 2) 
"""
等价于
add = decorator(add)
add(1, 2)
"""
```

## 执行顺序
洋葱法则 -- 从上至下

## Cataglogue

- [不带参数的函数装饰器](https://github.com/czp-first/ToBeBetter/tree/master/python/Decorator/func_no_args.py)
- [带参数的函数装饰器](https://github.com/czp-first/ToBeBetter/tree/master/python/Decorator/func_with_args.py)
- [不带参数的类装饰器](https://github.com/czp-first/ToBeBetter/tree/master/python/Decorator/cls_no_args.py)
- [带参数的类装饰器](https://github.com/czp-first/ToBeBetter/tree/master/python/Decorator/cls_with_args.py)


## Helpful
- [零基础学 Python（30）：装饰器的六种写法](https://iswbm.com/286.html)
