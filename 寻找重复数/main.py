class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for index in range(1, len(nums)):
            if nums[index - 1] == nums[index]:
                return nums[index]
