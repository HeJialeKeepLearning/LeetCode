# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        odd_list = []
        even_list = []
        for number in array:
            if number % 2 == 0:
                even_list.append(number)
            else:
                odd_list.append(number)
        return odd_list + even_list