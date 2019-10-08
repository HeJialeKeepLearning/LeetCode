class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        mid = (low + high) // 2
        while low < high - 1:
            if nums[mid] > nums[high]:
                low = mid
            else:
                high = mid
            mid = (low + high) // 2
        if nums[low] < nums[high]:
            return nums[low]
        return nums[high]