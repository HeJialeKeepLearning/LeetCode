# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        pleft, pright = 0, len(array) - 1
        while pleft < pright:
            cur_sum = array[pleft] + array[pright]
            if cur_sum == tsum:
                return [array[pleft], array[pright]]
            elif cur_sum < tsum:
                pleft += 1
            else:
                pright -= 1
        return []
