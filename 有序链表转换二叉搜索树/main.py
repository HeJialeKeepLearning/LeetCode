# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        slow, fast = head, head
        pre_slow = head
        while fast and fast.next:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        pre_slow.next = None
        if slow != fast:
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(slow.next)
        return root
