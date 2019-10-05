# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        plow, phigh = 1, 2
        ret_list = []
        while phigh > plow:
            cur_list = [i for i in range(plow, phigh + 1)]
            cur_sum = sum(cur_list)
            if cur_sum == tsum:
                ret_list.append(cur_list)
                plow += 1
            elif cur_sum > tsum:
                plow += 1
            else:
                phigh += 1

        return ret_list