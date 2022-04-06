exclusive OR(XOR)

无进位相加



```shell
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
```




# applications

```python
# swap a b
a, b = 11, 22
a = a ^ b
b = a ^ b
a = a ^ b
assert (a, b) == (22, 11)
```

## leetcode
- 136
- 260
