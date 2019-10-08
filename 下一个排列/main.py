class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        right_increase = [nums[-1]]
        for index in range(len(nums) - 2, -1, -1):
            if nums[index] >= right_increase[-1]:
                right_increase.append(nums[index])
            else:
                break
        if len(right_increase) == len(nums):
            nums.reverse()
            return
        switch = nums[index]
        for new_index in range(index, len(nums)):
            if new_index == len(nums) - 1 or switch >= nums[new_index + 1]:
                nums[index], nums[new_index] = nums[new_index], nums[index]
                nums[index + 1:] = sorted(nums[index + 1:])
                return

s = Solution()
s.nextPermutation([5, 1, 1])
