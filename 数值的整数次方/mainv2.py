# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        if exponent < 0:
            exponent = -exponent
            base = 1 / base
        exponent_bin = bin(exponent)[2:]
        exponent_bin = exponent_bin[::-1]
        exponent_list = []
        index = 0
        for i in exponent_bin:
            if i == '1':
                exponent_list.append(pow(2, index))
            index += 1

        ret_number = 1.0
        for ex in exponent_list:
            ret_number *= pow(base, int(ex))
        return ret_number

Solution.Power(Solution, 2, -3)
