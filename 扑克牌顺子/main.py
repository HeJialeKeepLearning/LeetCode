# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        zero_cnt, index = 0, 0
        numbers.sort()
        while index < len(numbers) - 1:
            if numbers[index] == 0:
                zero_cnt += 1
                index += 1
                continue
            if numbers[index] != numbers[index + 1] - 1:
                zero_cnt -= 1
                numbers.insert(index + 1, numbers[index] + 1)
            if zero_cnt < 0:
                return False
            index += 1
        return True
