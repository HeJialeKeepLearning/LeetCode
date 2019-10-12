class Solution:
    def findAnagrams(self, s, p):
        pattern_dict = {}
        for each_p in list(p):
            pattern_dict[each_p] = pattern_dict.get(each_p, 0) + 1
        ret_index = []
        s_list = list(s)
        # init sub_dict
        sub_dict = {}
        for sub_s in s_list[0:len(p)]:
            sub_dict[sub_s] = sub_dict.get(sub_s, 0) + 1
        for index in range(len(s) - len(p)):
            if sub_dict == pattern_dict:
                ret_index.append(index)
            sub_dict[s_list[index]] -= 1
            if not sub_dict[s_list[index]]:
                del sub_dict[s_list[index]]
            sub_dict[s_list[index + len(p)]] = sub_dict.get(s_list[index + len(p)], 0) + 1
        if sub_dict == pattern_dict:
            ret_index.append(index + 1)
        return ret_index
