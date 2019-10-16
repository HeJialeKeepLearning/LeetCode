class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        prev = None
        point_right = 0
        for index in range(len(nums)):
            if nums[index] == target:
                return True
            if not prev:
                prev = nums[index]
                continue
            if prev <= nums[index]:
                prev = nums[index]
            else:
                point_right = index
                break
        if nums[0] <= target <= nums[point_right]:
            low, high = 0, point_right
        else:
            low, high = point_right + 1, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return True
        return False