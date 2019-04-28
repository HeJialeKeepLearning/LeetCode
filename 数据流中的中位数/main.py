# -*- coding:utf-8 -*-
class Solution:
    datastream = []

    def Insert(self, num):
        # write code here
        self.datastream.append(num)
        self.datastream.sort()

    def GetMedian(self, data):
        # write code here
        if len(self.datastream) % 2:  # 奇数
            n = len(self.datastream) // 2
            return self.datastream[n]
        else:  # 偶数
            n = len(self.datastream) // 2
            return (self.datastream[n] + self.datastream[n - 1]) / 2.0
