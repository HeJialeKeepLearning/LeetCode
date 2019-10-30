class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_3, min_2 = nums[:3], nums[:2]
        for num in nums[2:]:
            min_2_max = max(min_2)
            if num < min_2_max:
                min_2.remove(min_2_max)
                min_2.append(num)
        for num in nums[3:]:
            max_3_min = min(max_3)
            if num > max_3_min:
                max_3.remove(max_3_min)
                max_3.append(num)
        result_min_2, result_max_3 = 1, 1
        for min_val in min_2:
            result_min_2 *= min_val
        result_min_2 *= max(max_3)
        for max_val in max_3:
            result_max_3 *= max_val
        return max(result_min_2, result_max_3)

