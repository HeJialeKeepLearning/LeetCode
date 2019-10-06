# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_dict = {}
        while head:
            if head in node_dict:
                return head
            node_dict[head] = 1
            head = head.next
        return