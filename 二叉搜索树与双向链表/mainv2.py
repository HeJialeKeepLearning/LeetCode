# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.pre = None

    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.in_order(pRootOfTree)
        return pRootOfTree

    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        root.left = self.pre
        if self.pre:
            self.pre.right = root
        self.pre = root
        self.in_order(root.right)

# root = TreeNode(10)
# root.left = TreeNode(6)
# root.right = TreeNode(14)
# left = root.left
# right = root.right
# left.left = TreeNode(4)
# left.right = TreeNode(8)
# right.left = TreeNode(12)
# right.right = TreeNode(16)
#
# s = Solution()
# s.Convert(root)