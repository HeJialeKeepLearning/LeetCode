# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        queue = [pRoot.left, pRoot.right]
        while queue:
            left, right = queue.pop(0), queue.pop(0)
            if (not left) or (not right):
                if left != right:
                    return False
                else:
                    continue
            elif left.val != right.val:
                return False
            queue.extend([left.left, right.right, left.right, right.left])
        return True