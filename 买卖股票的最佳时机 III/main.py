class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        K = 2
        dp = []
        for index1 in range(n + 1):
            cur_line = []
            for k in range(K + 1):
                cur_line.append({0: 0, 1: '-f'})
            dp.append(cur_line)
        for day_index in range(1, n + 1):
            for sale_k in range(1, len(dp[0])):
                if dp[day_index - 1][sale_k][1] != '-f':
                    dp[day_index][sale_k][0] = max(dp[day_index - 1][sale_k][0],
                                                   dp[day_index - 1][sale_k][1] + prices[day_index - 1])
                    dp[day_index][sale_k][1] = max(dp[day_index - 1][sale_k][1],
                                                   dp[day_index - 1][sale_k - 1][0] - prices[day_index - 1])
                else:
                    dp[day_index][sale_k][0] = dp[day_index - 1][sale_k][0]
                    dp[day_index][sale_k][1] = dp[day_index - 1][sale_k - 1][0] - prices[day_index - 1]
        return dp[-1][-1][0]
