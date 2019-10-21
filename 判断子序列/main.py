class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False
        dp = []
        for index_s in range(len(s)):
            row = []
            zero_flag = True
            for index_t in range(len(t)):
                if not dp:
                    if s[index_s] == t[index_t]:
                        row.append(1)
                        zero_flag = False
                    else:
                        row.append(0)
                else:
                    if s[index_s] == t[index_t]:
                        row.append(1 + max(dp[index_s - 1][:index_t]))
                        zero_flag = False
                    else:
                        row.append(0)
            if zero_flag:
                return False
            dp.append(row)
        match_length = max(dp[-1])
        return match_length == len(s)

