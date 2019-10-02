# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        dfs_stack = [root]
        output_list = []
        ret_list = []
        continue_pop_flag = False
        cur_sum = 0
        while dfs_stack:
            if continue_pop_flag:
                cur_sum -= output_list.pop().val
            p = dfs_stack.pop()
            continue_pop_flag = True
            output_list.append(p)
            cur_sum += p.val
            if cur_sum == expectNumber:
                if not p.left and not p.right:
                    ret_list.append([output.val for output in output_list])
                continue
            elif cur_sum > expectNumber:
                continue
            if p.left not in dfs_stack and p.left not in output_list:
                if p.left:
                    dfs_stack.append(p.left)
                    continue_pop_flag = False
            if p.right not in dfs_stack and p.right not in output_list:
                if p.right:
                    dfs_stack.append(p.right)
                    continue_pop_flag = False
        ret_list.sort(key = lambda l: len(l), reverse = True)
        return ret_list
