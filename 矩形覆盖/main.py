# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        a, b = 1, 2
        number -= 1
        while number:
            a, b = b, a + b
            number -= 1
        return a