# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if (not pRoot) or (k < 1):
            return
        inorder_list = self.in_order(pRoot)
        if k > len(inorder_list):
            return 
        return inorder_list[k-1]

    def in_order(self, root):
        if not root:
            return []
        ret_list = []
        ret_list.extend(self.in_order(root.left))
        ret_list.append(root)
        ret_list.extend(self.in_order(root.right))
        return ret_list
