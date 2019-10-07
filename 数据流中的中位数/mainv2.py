# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.maxheap = []
        self.minheap = []
    def Insert(self, num):
        if not self.maxheap:
            self.maxheap.append(num)
            return
        if num < self.maxheap[-1]:
            self.maxheap.append(num)
            self.maxheap.sort()
        else:
            self.minheap.append(num)
            self.minheap.sort(reverse = True)
        if abs(len(self.maxheap) - len(self.minheap)) > 1:
            if len(self.maxheap) > len(self.minheap):
                self.minheap.append(self.maxheap.pop())
                self.minheap.sort(reverse = True)
            else:
                self.maxheap.append(self.minheap.pop())
                self.maxheap.sort()
    def GetMedian(self):
        length = len(self.maxheap) + len(self.minheap)
        if length % 2:
            if len(self.maxheap) > len(self.minheap):
                return self.maxheap[-1]
            else:
                return self.minheap[-1]
        else:
            return (self.maxheap[-1] + self.minheap[-1]) / 2.0

