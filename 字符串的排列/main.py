# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if len(ss) == 1:
            return ss
        ret_list = set()
        ss = list(ss)
        for index in range(len(ss)):
            without_cur = ss[:index] + ss[index + 1:]
            sub_list = self.Permutation(''.join(without_cur))
            for sub_str in sub_list:
                ret_list.add(ss[index] + sub_str)
        return sorted(set(ret_list))
