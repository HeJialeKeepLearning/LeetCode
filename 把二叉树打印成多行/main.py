# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        retlist = [[pRoot.val]]
        queue = [pRoot]
        right = pRoot
        while queue:
            p = queue.pop(0)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
            if right == p:
                if not queue:
                    break
                retlist.append([node.val for node in queue])
                right = queue[-1]
        return retlist