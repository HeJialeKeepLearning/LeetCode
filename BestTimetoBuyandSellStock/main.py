class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0
        minprice = prices[0]
        maxprofit = prices[1] - prices[0]
        for currentprice in prices[1:]:
            if currentprice < minprice:
                minprice = currentprice
            elif currentprice - minprice > maxprofit:
                maxprofit = currentprice - minprice
        if maxprofit < 0:
            return 0
        else:
            return maxprofit
