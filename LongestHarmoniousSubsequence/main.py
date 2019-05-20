import collections

class Solution:
    def findLHS(self, nums):
        deldup = list(set(nums))  # 去掉重复元素
        deldup.sort()
        countlist = []
        length = [0]
        for i in range(1, len(deldup)):
            if deldup[i] == deldup[i - 1] + 1:
                countlist.append([deldup[i - 1], deldup[i]])
        counter = collections.Counter(nums)
        for sublist in countlist:
            length.append(abs(counter[sublist[0]] + counter[sublist[1]]))
        return max(length)

Solution.findLHS(Solution,[1,4,1,3,1,-14,1,-13])