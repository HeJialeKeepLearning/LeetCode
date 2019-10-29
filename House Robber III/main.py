# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def tree_dp(root):
            if not root:
                # list[0]代表不打劫该节点，list[1]代表打劫该节点
                return [0, 0]
            left = tree_dp(root.left)
            right = tree_dp(root.right)

            return [max(left) + max(right), root.val + left[0] + right[0]]
        return max(tree_dp(root))
