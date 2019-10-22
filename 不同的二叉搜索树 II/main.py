# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def recursive_generate(node_val_list):
            if not node_val_list:
                return [None]
            ret_list = []
            for index in range(len(node_val_list)):
                left_list = recursive_generate(node_val_list[:index])
                right_list = recursive_generate(node_val_list[index + 1:])
                for left_node in left_list:
                    for right_node in right_list:
                        cur_root = TreeNode(node_val_list[index])
                        cur_root.left = left_node
                        cur_root.right = right_node
                        ret_list.append(cur_root)
            return ret_list

        return recursive_generate([i for i in range(1, n + 1)]) if n else []

