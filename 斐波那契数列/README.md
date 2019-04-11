## 解题思路
尝试使用field,发现效果并不好，因为yield返回一个可迭代对象，而题目只需要输出第n个数，所以还不如普通计算呢
<br>输出数列第n个数的版本:
```python
def Fibonacci(n):
    k, a, b = 0, 0, 1
    while k < n:
        a, b = b, a + b
        k += 1
    return a
```