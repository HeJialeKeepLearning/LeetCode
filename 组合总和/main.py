class Solution:
    def combinationSum(self, candidates, target):
        dp = [[[]]]
        index = 1
        while index <= target:
            cur_list = []
            for candidate in candidates:
                if (index - candidate >= 0) and (dp[index - candidate] != None):
                    for sub_list in dp[index - candidate]:
                        tmp_list = sub_list.copy()
                        tmp_list.append(candidate)
                        tmp_list.sort()
                        if tmp_list not in cur_list:
                            cur_list.append(tmp_list)
            if not cur_list:
                dp.append(None)
            else:
                dp.append(cur_list)
            index += 1
        return dp[-1]
