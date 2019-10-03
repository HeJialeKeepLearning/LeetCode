# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        path_list = self.dfs(pRoot)
        return len(max(path_list, key = len))

    def dfs(self, root):
        if not root:
            return [[]]
        if (not root.left) and (not root.right):
            return [[root.val]]
        path = []
        left_paths = self.dfs(root.left)
        right_paths = self.dfs(root.right)
        for each_path in left_paths:
            cur_path = [root.val]
            cur_path.extend(each_path)
            path.append(cur_path)
        for each_path in right_paths:
            cur_path = [root.val]
            cur_path.extend(each_path)
            path.append(cur_path)
        return path

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
s.TreeDepth(root)