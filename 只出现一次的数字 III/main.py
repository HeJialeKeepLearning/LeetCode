class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        aux_dict = {}
        for num in nums:
            if num in aux_dict:
                aux_dict.pop(num)
            else:
                aux_dict[num] = 1
        return [aux_dict.popitem()[0], aux_dict.popitem()[0]]
