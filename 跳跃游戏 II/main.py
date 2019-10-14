class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        dp = [nums[0]]
        index = 1
        while index < len(nums) - 1:
            if dp[-1] >= len(nums) - 1:
                break
            new_dp, new_dp_index = nums[index], index
            for num_index in range(index, dp[-1] + 1):
                if nums[num_index] + num_index >= new_dp:
                    new_dp = nums[num_index] + num_index
            index = dp[-1] + 1
            dp.append(new_dp)
        return len(dp)