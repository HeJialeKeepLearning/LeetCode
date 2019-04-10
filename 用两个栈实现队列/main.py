# -*- coding:utf-8 -*-
stack1 = []
stack2 = []

class Solution:

    def push(self, node):
        while len(stack2) != 0:
            stack1.append(stack2.pop())
        stack1.append(node)

    def pop(self):
        while len(stack1) != 0:
            stack2.append(stack1.pop())
        return stack2.pop()