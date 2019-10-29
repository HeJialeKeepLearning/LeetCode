class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, 0, 0]
        for num in nums:
            dp.append(num + max(dp[-2], dp[-3]))
        return max(dp)
