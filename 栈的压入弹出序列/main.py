# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        for pop_e in popV:
            pop_index = popV.index(pop_e)
            if pop_e not in pushV:
                return False
            push_index = pushV.index(pop_e)
            both_pop = [x for x in popV[pop_index + 1:] if x in pushV[:push_index]]
            both_push = [x for x in pushV[:push_index] if x in popV[pop_index + 1:]]

            both_push.reverse()
            if both_pop != both_push:
                return False
        return True
