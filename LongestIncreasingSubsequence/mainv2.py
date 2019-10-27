class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1]
        for index in range(1, len(nums)):
            candidates = []
            for prev_index in range(index):
                if nums[index] > nums[prev_index]:
                    candidates.append(dp[prev_index])
            dp.append(1 + max(candidates) if candidates else 1)
        return max(dp)
