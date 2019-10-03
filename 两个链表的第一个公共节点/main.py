# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        len1, len2 = 0, 0
        p1, p2 = pHead1, pHead2
        while p1:
            len1 += 1
            p1 = p1.next
        while p2:
            len2 += 1
            p2 = p2.next
        if len1 > len2:
            longp = pHead1
            shortp = pHead2
        else:
            longp = pHead2
            shortp = pHead1
        diff = abs(len1 - len2)
        while diff:
            longp = longp.next
            diff -= 1
        while longp:
            if longp == shortp:
                return longp
            longp = longp.next
            shortp = shortp.next