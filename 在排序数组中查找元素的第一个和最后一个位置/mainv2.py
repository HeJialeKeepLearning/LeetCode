class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.left_bound(nums, target), self.right_bound(nums, target)]

    def left_bound(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        if low < len(nums) and nums[low] == target:
            return low
        return -1

    def right_bound(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        if high >= 0 and nums[high] == target:
            return high
        return -1