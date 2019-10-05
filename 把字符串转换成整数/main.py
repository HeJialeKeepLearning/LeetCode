# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        op = s[0]
        if op in ['+', '-']:
            s = s[1:]
        if not s.isdigit():
            return 0
        num = 0
        for char in s:
                num = num * 10 + int(char)
        maxint = pow(2, 31)
        if num > maxint or (op != '-' and num > maxint - 1):
            return 0
        if op == '-':
            return -num
        return num

