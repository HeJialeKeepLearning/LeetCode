# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val > pHead2.val:
            ret_head = ListNode(pHead2.val)
            pHead2 = pHead2.next
        else:
            ret_head = ListNode(pHead1.val)
            pHead1 = pHead1.next
        p = ret_head
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                p.next = ListNode(pHead1.val)
                pHead1 = pHead1.next
            else:
                p.next = ListNode(pHead2.val)
                pHead2 = pHead2.next
            p = p.next
        while pHead1:
            p.next = ListNode(pHead1.val)
            pHead1 = pHead1.next
            p = p.next
        while pHead2:
            p.next = ListNode(pHead2.val)
            pHead2 = pHead2.next
            p = p.next
        return ret_head
