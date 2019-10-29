class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        dp_1, dp_2 = 0, 0
        for num in nums[:-1]:
            dp_1, dp_2 = max(dp_2 + num, dp_1), dp_1
        p_max = dp_1
        dp_1, dp_2 = 0, 0
        for num in nums[:0:-1]:
            dp_1, dp_2 = max(dp_2 + num, dp_1), dp_1
        n_max = dp_1
        return max(p_max, n_max)