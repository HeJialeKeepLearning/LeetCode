class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high - 1:
            mid = (low + high) // 2
            if nums[high] == nums[mid]:
                high -= 1
                continue
            if nums[low] == nums[mid]:
                low += 1
                continue
            if nums[mid] > nums[high]:
                low = mid
            else:
                high = mid
        if high == len(nums) - 1:
            return min(nums[low], nums[high])
        return min(nums[low], nums[high], nums[high + 1])