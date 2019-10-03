class Solution:
    def nthUglyNumber(self, n):
        dp = [0] * n
        dp[0] = 1
        p_2, p_3, p_5 = 0, 0, 0
        for index in range(1, n):
            dp[index] = min(dp[p_2] * 2, dp[p_3] * 3, dp[p_5] * 5)
            if dp[index] == dp[p_2] * 2:
                p_2 += 1
            if dp[index] == dp[p_3] * 3:
                p_3 += 1
            if dp[index] == dp[p_5] * 5:
                p_5 += 1
        return dp[-1]
