class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return
        sumvalue = nums[0]
        maxvalue = sumvalue
        for i in range(1, len(nums)):
            if sumvalue < 0:
                sumvalue = nums[i]
            else:
                sumvalue += nums[i]
            if maxvalue < sumvalue:
                maxvalue = sumvalue
        return maxvalue
