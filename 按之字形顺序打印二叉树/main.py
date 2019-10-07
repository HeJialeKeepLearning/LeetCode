# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        queue = [pRoot]
        ret_list = [[pRoot.val]]
        height = 0
        right = pRoot
        while queue:
            p = queue.pop(0)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
            if right == p:
                height += 1
                if not queue:
                    break
                right = queue[-1]
                if height % 2:
                    ret_list.append([node.val for node in queue[::-1]])
                else:
                    ret_list.append([node.val for node in queue])
        return ret_list
