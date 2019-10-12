class Solution:
    def groupAnagrams(self, strs):
        set_dict = {}
        for each_str in strs:
            cur_stat = ''.join(sorted(list(each_str)))
            if cur_stat not in set_dict:
                set_dict[cur_stat] = [each_str]
            else:
                set_dict[cur_stat].append(each_str)
        return list(set_dict.values())