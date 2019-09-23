class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        ret_list = []
        for start in range(len(nums) - 3):
            for substart in range(start+1, len(nums) - 2):
                i = substart + 1
                j = len(nums) - 1
                while i < j:
                    cur_sum = nums[start] + nums[substart] + nums[i] + nums[j]
                    if cur_sum == target:
                        res = [nums[start],nums[substart],nums[i],nums[j]]
                        if res not in ret_list:
                            ret_list.append(res)
                        i += 1
                        j -= 1
                    elif cur_sum < target:
                        i += 1
                    else:
                        j -= 1
        return ret_list