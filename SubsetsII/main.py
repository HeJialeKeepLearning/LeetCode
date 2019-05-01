import copy

class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [[], nums]
        nums.sort()
        frest = copy.deepcopy(nums)
        first = frest.pop()
        resultlist = [[], [first]]  # 保存末尾字母作为子集
        nextlists = self.subsetsWithDup(Solution, frest)  # 下层返回值
        for nextlist in nextlists:
            if nextlist not in resultlist:
                resultlist.append(nextlist)  # 把下层的子集放入
            tmp = nextlist[:]
            tmp.append(first)  # 把本层的末尾字母加入下层子集
            if tmp not in resultlist:
                resultlist.append(tmp)  # 把加了末尾字母的子集放入
        return resultlist

# Solution.subsetsWithDup(Solution, [1, 2, 2])
