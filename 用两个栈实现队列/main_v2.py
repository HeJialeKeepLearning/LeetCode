# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack_push = []
        self.stack_pop = []
    def push(self, node):
        self.stack_push.append(node)
    def pop(self):
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop.pop()