# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.cur_min = None
    def push(self, node):
        if not self.stack: # first push
            self.stack.append(node)
            self.min_stack.append(node)
            self.cur_min = node
            return
        self.stack.append(node)
        self.cur_min = self.min_stack[-1]
        if self.cur_min > node:
            self.min_stack.append(node)
            self.cur_min = node
    def pop(self):
        pop_e = self.stack.pop()
        if pop_e == self.cur_min:
            self.min_stack.pop()
            self.cur_min = self.min_stack[-1]
        return pop_e
    def top(self):
        return self.stack[-1]
    def min(self):
        return self.cur_min
