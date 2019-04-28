# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    dic = {}

    def FirstAppearingOnce(self):
        # write code here
        for k in self.dic.keys():
            if self.dic[k] == 1:
                return k
        return '#'

    def Insert(self, char):
        # write code here
        if char in Solution.dic:
            Solution.dic[char] += 1
        else:
            Solution.dic[char] = 1
