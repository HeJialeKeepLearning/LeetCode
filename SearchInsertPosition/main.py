class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            for n in nums:
                if n > target:
                    return nums.index(n)
            return len(nums)
