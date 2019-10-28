class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 前面的数字代表交易次数，后面的数字代表是否持有股票
        dp1_0, dp1_1 = 0, '-f'
        dp2_0, dp2_1 = 0, '-f'
        for price in prices:
            if dp1_1 != '-f' and dp2_1 != '-f':
                dp2_0 = max(dp2_0, dp2_1 + price)
                dp2_1 = max(dp2_1, dp1_0 - price)
                dp1_0 = max(dp1_0, dp1_1 + price)
                dp1_1 = max(dp1_1, -price)
            else:
                dp2_1 = dp1_0 - price
                dp1_1 = -price
        return dp2_0
