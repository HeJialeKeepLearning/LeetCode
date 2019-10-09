class Solution:
    def searchRange(self, nums, target):
        target_index = -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                target_index = mid
                break
        if target_index < 0:
            return [-1, -1]
        low, high = target_index, target_index
        while low >= 0 and nums[low] == target:
            low -= 1
        while high < len(nums) and nums[high] == target:
            high += 1
        return [low + 1, high - 1]
