import sys

class Solution:
    def threeSumClosest(self, nums, target):
        closest_sum = None
        sum_dif = sys.maxsize
        nums.sort()
        for start in range(len(nums) - 2):
            left = start + 1
            right = len(nums) - 1
            while left < right:
                cur_sum = nums[start] + nums[left] + nums[right]
                cur_dif = abs(cur_sum - target)
                if cur_dif < sum_dif:  # update closest_sum
                    closest_sum = cur_sum
                    sum_dif = cur_dif
                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    return target
        return closest_sum

# Solution.threeSumClosest(Solution, [0, 2, 1, -3], 1)
