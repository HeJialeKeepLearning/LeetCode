# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        p, q = 0, 1
        while n > 1:
            p, q = q, p + q
            n -= 1
        return q
