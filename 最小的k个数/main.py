# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput) or k == 0:
            return []
        min_window = tinput[:k]
        if len(min_window) < k:
            return min_window
        for element in tinput[k:]:
            cur_max = max(min_window)
            if cur_max > element:
                min_window.remove(cur_max)
                min_window.append(element)
        return sorted(min_window)

