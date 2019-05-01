import copy

class Solution:
    def subsets(self, nums):
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [[], nums]
        frest = copy.deepcopy(nums)
        first = frest.pop()
        resultlist = [[], [first]]  # 保存末尾字母作为子集
        nextlists = self.subsets(frest)
        for nextlist in nextlists:
            if nextlist not in resultlist:
                resultlist.append(nextlist)  # 先把下一层的子集放进去
                tmp = nextlist[:]
                tmp.append(first)  # 再向该子集增加本层末尾字母
                resultlist.append(tmp)  # 最后把增加了末尾字母的子集放进去
        return resultlist
