class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dp = []
        for num in nums:
            if not dp:
                dp.append([[num]])
                continue
            new_dp = []
            for old_permute in dp[-1]:
                for index in range(len(old_permute) + 1):
                    old_permute.insert(index, num)
                    new_dp.append(old_permute[:])
                    old_permute.remove(num)
            dp.append(new_dp)
        return dp[-1] if nums else [[]]
