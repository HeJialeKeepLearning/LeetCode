# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head:
            return head
        p, q = head, head
        k -= 1
        while k:
            q = q.next
            if not q:
                return q
            k -= 1
        while q.next:
            p = p.next
            q = q.next
        return p
