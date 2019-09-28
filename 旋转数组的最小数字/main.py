# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        for i in range(1, len(rotateArray)):
            if rotateArray[i - 1] > rotateArray[i]:
                return rotateArray[i]