# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
        # get list length
        length_node = head
        length = 0
        while length_node:
            length += 1
            length_node = length_node.next
        p, q = head, head
        k = k % length
        if k == 0:
            return head
        while k:
            q = q.next
            k -= 1
            length += 1
        while q.next:
            p = p.next
            q = q.next
            length += 1
        ret_head = p.next
        p.next = None
        q.next = head
        return ret_head