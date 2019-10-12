class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}
        for each_s in list(s):
            s_dict[each_s] = s_dict.get(each_s, 0) + 1
        for each_t in list(t):
            t_dict[each_t] = t_dict.get(each_t, 0) + 1
        return s_dict == t_dict