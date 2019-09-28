# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        prev_sum = 0
        while number:
            cur = prev_sum + 1
            prev_sum += cur
            number -= 1
        return cur

class Solution2:
    def jumpFloorII(self, number):
        if number == 1:
            return 1
        return 2 << (number - 2)