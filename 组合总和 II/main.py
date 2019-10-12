class Solution:
    def combinationSum2(self, candidates, target):
        if target == 0:
            return [[]]
        if target < 0 or len(candidates) <= 0:
            return None
        ret_list = []
        candidate_set = set()
        for index in range(len(candidates)):
            if candidates[index] not in candidate_set:
                candidate_set.add(candidates[index])
            else:
                continue
            sub_list = self.combinationSum2(candidates[0:index] + candidates[index + 1:], target - candidates[index])
            if sub_list == None:
                continue
            for sub in sub_list:
                sub.append(candidates[index])
                sub.sort()
                if sub not in ret_list:
                    ret_list.append(sub)

        return ret_list

