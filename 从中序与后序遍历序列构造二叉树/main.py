# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        root_index = inorder.index(root.val)
        left_length = len(inorder[:root_index])
        root.left = self.buildTree(inorder[:root_index], postorder[:left_length])
        root.right = self.buildTree(inorder[root_index + 1:], postorder[left_length:-1])
        return root
