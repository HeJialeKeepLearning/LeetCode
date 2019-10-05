# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n == 0:
            return -1
        length = n
        child_numbers = [i for i in range(n)]
        out_index = (m - 1) % length
        while length > 1:
            child_numbers.pop(out_index)
            length -= 1
            out_index = (out_index + m - 1) % length
        return child_numbers[0]
