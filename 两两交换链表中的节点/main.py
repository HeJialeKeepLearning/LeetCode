# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        if not head:
            return head
        p, q = head, head.next
        if (not p) or (not q):
            return head
        ret_head = q
        # swap first two
        pair_next = q.next
        q.next = p
        p.next = pair_next
        pair_prev = p
        p = pair_next
        if not p:
            return ret_head
        q = p.next
        while (p and q):
            try:
                pair_next = q.next
                q.next = p
                p.next = pair_next
                pair_prev.next = q
                pair_prev = p
                p = pair_next
                q = p.next
            except AttributeError:
                break

        return ret_head
