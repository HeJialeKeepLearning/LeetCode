# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ordered_list = []
        p = head
        while p:
            ordered_list.append(p.val)
            p = p.next
        ordered_list.sort(reverse = True)
        p = head
        while p:
            p.val = ordered_list.pop(-1)
            p = p.next
        return head