# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum_list = self.dfs_sum(root)
        if sum in sum_list:
            return True
        return False

    def dfs_sum(self, root):
        if not root:
            return ['EB90']
        if (not root.left) and (not root.right):
            return [root.val]
        sub_sum = self.dfs_sum(root.left) + self.dfs_sum(root.right)
        return [root.val + sub_num for sub_num in sub_sum if sub_num != 'EB90']
