# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return
        node_dict = {}
        clone_head = RandomListNode(pHead.label)
        cur_p = clone_head
        ori_p = pHead
        node_dict[cur_p.label] = cur_p
        while ori_p.next:
            cur_p.next = RandomListNode(ori_p.next.label)
            cur_p = cur_p.next
            ori_p = ori_p.next
            node_dict[cur_p.label] = cur_p

        cur_p = clone_head
        ori_p = pHead
        while cur_p:
            if not ori_p.random:
                cur_p.random = None
            else:
                cur_p.random = node_dict[ori_p.random.label]
            cur_p = cur_p.next
            ori_p = ori_p.next

        return clone_head
