class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        # 找出旋转点index
        low, high = 0, len(nums) - 1
        mid = (low + high) // 2
        while low < high - 1:
            if nums[mid] > nums[high]:
                low = mid
            else:
                high = mid
            mid = (low + high) // 2
        # 判断target落在哪一段
        if nums[0] <= target <= nums[mid]:
            low, high = 0, low
        else:
            low, high = high, len(nums) - 1
        mid = (low + high) // 2
        # 二分查找
        while low < high - 1:
            if target > nums[mid]:
                low = mid
            else:
                high = mid
            mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        if mid + 1 == len(nums):
            return -1
        if target == nums[mid + 1]:
            return mid + 1
        return -1

