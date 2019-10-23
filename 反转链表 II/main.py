# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        cnt = 1
        init_head = ListNode(-1)
        prev = init_head
        prev.next = head
        p = head
        while p:
            if cnt == m:
                start = prev
            if cnt == n:
                end = p.next
            prev, p = p, p.next
            cnt += 1
        p = start.next
        node_val = []
        while p != end:
            node_val.append(p.val)
            p = p.next
        node_val.reverse()
        for each_val in node_val:
            start.next.val = each_val
            start = start.next
        return init_head.next
