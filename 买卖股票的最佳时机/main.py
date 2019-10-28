class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        for each_price in prices:
            if each_price - min_price > max_profit:
                max_profit = each_price - min_price
            if each_price < min_price:
                min_price = each_price
        return max_profit
