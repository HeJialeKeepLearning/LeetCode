# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        height, balance = self.post_order(pRoot)
        return balance

    def post_order(self, root):
        if not root:
            return 0, True
        if (not root.left) and (not root.right):
            return 1, True

        left_height, left_balance = self.post_order(root.left)
        right_height, right_balance = self.post_order(root.right)
        if (not(left_balance & right_balance)) or (abs(left_height - right_height) > 1):
            return max(left_height, right_height) + 1, False
        return max(left_height, right_height) + 1, True
