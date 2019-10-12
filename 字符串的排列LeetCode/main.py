class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern_dict = {}
        for sub_s in list(s1):
            pattern_dict[sub_s] = pattern_dict.get(sub_s, 0) + 1
        long_dict = {}
        # init long_dict
        s2_list = list(s2)
        for sub_s in s2_list[:len(s1)]:
            long_dict[sub_s] = long_dict.get(sub_s, 0) + 1
        for index in range(len(s1), len(s2)):
            if long_dict == pattern_dict:
                return True
            long_dict[s2_list[index - len(s1)]] -= 1
            if not long_dict[s2_list[index - len(s1)]]:
                del long_dict[s2_list[index - len(s1)]]
            long_dict[s2_list[index]] = long_dict.get(s2_list[index], 0) + 1
        if long_dict == pattern_dict:
            return True
        return False