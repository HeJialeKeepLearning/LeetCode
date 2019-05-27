class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        f = [nums[0], nums[1]]
        for i in range(2, len(nums)):
            f.append(max(f[:-1]) + nums[i])
        return max(f)
