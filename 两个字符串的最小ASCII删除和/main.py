class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
        for index in range(1, len(dp[0])):
            dp[0][index] = ord(s1[index - 1]) + dp[0][index - 1]
        for index in range(1, len(dp)):
            dp[index][0] = ord(s2[index - 1]) + dp[index - 1][0]

        for row_index in range(1, len(dp)):
            for col_index in range(1, len(dp[0])):
                if s1[col_index - 1] == s2[row_index - 1]:
                    dp[row_index][col_index] = dp[row_index - 1][col_index - 1]
                else:
                    dp[row_index][col_index] = min(dp[row_index - 1][col_index] + ord(s2[row_index - 1]),
                                                   dp[row_index][col_index - 1] + ord(s1[col_index - 1]))
        return dp[-1][-1]
