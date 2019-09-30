# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        val_list = []
        p = pHead
        while p:
            val_list.append(p.val)
            p = p.next
        val_list.reverse()
        p = pHead
        for val in val_list:
            p.val = val
            p = p.next
        return pHead