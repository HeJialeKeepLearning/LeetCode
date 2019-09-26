class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mark_dict = {}
        for num in nums:
            if num in mark_dict:
                mark_dict.pop(num)
            else:
                mark_dict[num] = 1

        return mark_dict.popitem()[0]