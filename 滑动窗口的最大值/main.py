# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not size:
            return []
        elif size > len(num):
            return []
        maxlist = []
        currentwindow = num[:size]
        currentmax = max(currentwindow)
        maxlist.append(currentmax)
        for n in num[size:]:
            pope = currentwindow.pop(0)
            currentwindow.append(n)
            if n >= currentmax:  # 如果新的元素比当前最大值还大
                currentmax = n
            elif pope == currentmax:  # 如果把最大值滑掉了
                currentmax = max(currentwindow)
            maxlist.append(currentmax)
        return maxlist
