# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        s_parts = s.split(' ')
        s_parts.reverse()
        return ' '.join(s_parts)