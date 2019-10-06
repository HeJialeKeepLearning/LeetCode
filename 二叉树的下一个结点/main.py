# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # 判断是否有右子树
        if pNode.right:
            # 有右子树，找最左边的节点
            p = pNode.right
            while p.left:
                p = p.left
            return p
        # pNode无右子树
        root = pNode
        grad_root = root.next
        while grad_root and root != grad_root.left:
            root = grad_root
            grad_root = grad_root.next
        return grad_root