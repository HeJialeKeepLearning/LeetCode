class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n] * m
        for sub_m in range(0, m):
            for sub_n in range(0, n):
                if not (sub_m and sub_n):
                    dp[sub_m][sub_n] = 1
                else:
                    dp[sub_m][sub_n] = dp[sub_m - 1][sub_n] + dp[sub_m][sub_n - 1]

        return dp[-1][-1]
