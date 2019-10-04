# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        element_list = []
        for element in array:
            if element in element_list:
                element_list.remove(element)
            else:
                element_list.append(element)
        return element_list