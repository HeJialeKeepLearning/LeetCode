class Solution:
    def canJump(self, nums):
        dp = [nums[0]]
        for index in range(1, len(nums) - 1):
            new_dp = max(dp[-1], nums[index] + index)
            if new_dp > dp[-1] and index <= dp[-1]:
                dp.append(new_dp)
            if dp[-1] >= len(nums) - 1:
                return True
        return False
