# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        cnt = 0
        for each_data in data:
            if cnt and (each_data != k):
                return cnt
            if each_data == k:
                cnt += 1
        return cnt
