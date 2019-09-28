# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        root = TreeNode(pre[0])  # 记录根节点
        if root:
            rootIndex = tin.index(root.val)  # 找到根节点在中序遍历中的索引index
            root.left = self.reConstructBinaryTree(pre[1:1 + rootIndex], tin[:rootIndex])
            root.right = self.reConstructBinaryTree(pre[rootIndex + 1:], tin[rootIndex + 1:])
        return root