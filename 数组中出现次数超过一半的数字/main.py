# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        number_dict = {}
        for number in numbers:
            number_dict[number] = number_dict.get(number, 0) + 1
            if number_dict[number] > len(numbers) / 2:
                return number
        return 0
