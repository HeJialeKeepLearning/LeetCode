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
        queue = [pRoot]
        right = pRoot
        while queue:
            p = queue.pop(0)
            if p.val != '#': # 如果当前不是空节点，则给空子树插入空节点
                if not p.left:
                    p.left = TreeNode('#')
                if not p.right:
                    p.right = TreeNode('#')
                queue.append(p.left)
                queue.append(p.right)
            if right == p:
                if not self.is_list_symmetrical(queue):
                    return False
                if not queue:
                    break
                right = queue[-1]
        return True

    def is_list_symmetrical(self, queue):
        if len(queue) % 2:  # 长度为奇数
            return False
        left, right = len(queue) // 2 - 1, len(queue) // 2
        while left >= 0:
            if (not queue[left]) or (not queue[right]): # None
                if queue[left] == queue[right]:
                    left -= 1
                    right += 1
                    continue
                else:
                    return False
            if queue[left].val != queue[right].val:
                return False
            left -= 1
            right += 1
        return True

