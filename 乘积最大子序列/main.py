class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret_max = nums[0]
        cur_max, cur_min = 1, 1
        for num in nums:
            if num < 0:
                cur_max, cur_min = max(cur_min * num, num), min(cur_max * num, num)
            else:
                cur_max, cur_min = max(cur_max * num, num), min(cur_min * num, num)
            ret_max = max(ret_max, cur_max)
        return ret_max
