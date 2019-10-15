class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        color_dict = {}
        for num in nums:
            color_dict[num] = color_dict.get(num, 0) + 1
        del nums[:]
        for num in [0, 1, 2]:
            if num not in color_dict:
                continue
            nums += [num] * color_dict[num]
