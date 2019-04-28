# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead.next:  # 如果只有1个节点
            return pHead
        pre = pHead
        p = pre.next
        dic = {}
        dic[pre.val] = 1
        while p:
            if p.val in dic:  # 如果重复
                pre.next = p.next
                p = pre.next
                dic[pre.val] = '#'  # 标记，后续删除pre对应的节点
            else:
                dic[p.val] = 1
                pre = p
                p = p.next
        # 保证pHead对应的节点是需要保留的
        while dic[pHead.val] == '#':
            pHead = pHead.next
        p = pHead
        while p:
            if dic[p.next.val] == '#':
                pre = p.next
                p.next = pre.next
            else:
                p = p.next
        return pHead
