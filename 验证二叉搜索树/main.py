# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        mid_order = []
        stack = [(0, root)]
        while stack:
            p_stat, p = stack.pop()
            if not p:
                continue
            if p_stat == 0:
                stack.append((0, p.right))
                stack.append((1, p))
                stack.append((0, p.left))
            else:
                mid_order.append(p.val)
        prev = mid_order[0]
        for each_val in mid_order[1:]:
            if each_val > prev:
                prev = each_val
            else:
                return False
        return True
