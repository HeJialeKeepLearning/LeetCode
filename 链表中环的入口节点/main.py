# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        marklist=[]
        while pHead:
            if pHead in marklist:
                return pHead
            else:
                marklist.append(pHead)
                pHead = pHead.next
        return
