# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        cur_sum = array[0]
        ret_sum = array[0]
        for element in array[1:]:
            if cur_sum > 0:
                cur_sum += element
            else:
                cur_sum = element
            ret_sum = max(ret_sum, cur_sum)
        return ret_sum
