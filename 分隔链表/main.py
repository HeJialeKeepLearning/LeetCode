# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        ret_head = ListNode(-1)
        ret_head.next = head
        small = ret_head
        prev, p = small, head
        while p:
            if p.val < x:
                if small.next != p:
                    prev.next = p.next
                    p.next = small.next
                    small.next = p
                    small = small.next
                    p = prev.next
                    continue
                else:
                    small = p
            prev, p = p, p.next
        return ret_head.next
