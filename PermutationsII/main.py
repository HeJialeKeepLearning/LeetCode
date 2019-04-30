class Solution:
    def permuteUnique(self, nums):
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [nums]
        resultlist = []
        length = len(nums)
        index = 0
        flaglist = []  # 记录首字母
        while index < length:
            n = nums[index]
            while n in flaglist:
                index += 1
                if index == length:
                    break
                n = nums[index]
            else:
                flaglist.append(n)
            if index >= length:
                break
            numscopy = nums[:]
            del numscopy[index]
            nextresult = self.permuteUnique(numscopy)
            for nextresultline in nextresult:
                currentlist = [n]
                for nextresulte in nextresultline:
                    currentlist.append(nextresulte)
                resultlist.append(currentlist)
            index += 1
        return resultlist
