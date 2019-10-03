# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        queue = [pRoot]
        depth = 0
        right_p = pRoot
        while queue:
            p = queue[0]
            queue.remove(p)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
            if right_p == p:
                depth += 1
                if not queue:
                    return depth
                right_p = queue[-1]
