# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        ret_head = ListNode(-1)
        ret_head.next = head
        prev, p = ret_head, head
        dup_flag = False
        while p.next:
            if p.val != p.next.val:
                if dup_flag:
                    prev.next = p.next
                    dup_flag = False
                else:
                    prev = p
                p = p.next
            else:
                p = p.next
                dup_flag = True
        if dup_flag:
            prev.next = p.next
        return ret_head.next
