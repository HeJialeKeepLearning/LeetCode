# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        len1, len2 = 0, 0
        p1, p2 = pHead1, pHead2
        while p1:
            len1 += 1
            p1 = p1.next
        while p2:
            len2 += 1
            p2 = p2.next
        while len1 - len2 > 0:
            pHead1 = pHead1.next
            len1 -= 1
        while len2 - len1 > 0:
            pHead2 = pHead2.next
            len2 -= 1
        while pHead1:
            if pHead1.val == pHead2.val:
                return pHead1
            else:
                pHead1 = pHead1.next
                pHead2 = pHead2.next
