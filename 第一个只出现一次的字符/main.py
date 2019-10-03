# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        occur_dict = {}
        for string in s:
            occur_dict[string] = occur_dict.get(string, 0) + 1
        for string in s:
            if occur_dict[string] == 1:
                return s.index(string)
        return -1