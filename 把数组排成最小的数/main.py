# -*- coding:utf-8 -*-
from functools import cmp_to_key

class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        numbers.sort(key = cmp_to_key(lambda n1, n2: int(str(n1) + str(n2)) - int(str(n2) + str(n1))))
        return ''.join(str(number) for number in numbers)
