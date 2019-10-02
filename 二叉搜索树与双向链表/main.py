# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.node_dict = {}
        self.node_list = []

    def Convert(self, pRootOfTree):
        if not pRootOfTree.left or not pRootOfTree:
            if pRootOfTree.left:
                pRootOfTree.left.right = pRootOfTree
            if pRootOfTree.right:
                pRootOfTree.right.left = pRootOfTree
            return pRootOfTree
        self.in_order(pRootOfTree)
        for index in range(1, len(self.node_list) - 1):
            node = self.node_dict[self.node_list[index]]
            node.left = self.node_dict[self.node_list[index - 1]]
            node.right = self.node_dict[self.node_list[index + 1]]
        head = self.node_dict[self.node_list[0]]
        head.left = None
        head.right = self.node_dict[self.node_list[1]]
        tail = self.node_dict[self.node_list[-1]]
        tail.right = None
        tail.left = self.node_dict[self.node_list[-2]]
        return pRootOfTree

    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        self.node_dict[root.val] = root
        self.node_list.append(root.val)
        self.in_order(root.right)