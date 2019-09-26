class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        aux_dict = {}
        for num in nums:
            if num in aux_dict:
                aux_dict[num] = aux_dict.get(num) + 1
                if aux_dict[num] == 3:
                    aux_dict.pop(num)
            else:
                aux_dict[num] = 1
        return aux_dict.popitem()[0]
