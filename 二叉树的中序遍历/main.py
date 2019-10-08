# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        white, grey = 0, 1
        stack = [(white, root)]
        result = []
        while stack:
            color, p = stack.pop()
            if not p:
                continue
            if color == white:
                stack.append((white, p.right))
                stack.append((grey, p))
                stack.append((white, p.left))
            else:
                result.append(p.val)
        return result