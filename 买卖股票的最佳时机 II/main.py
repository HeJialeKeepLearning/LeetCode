class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [0]
        for index in range(1, len(prices)):
            candidates = []
            for prev_index in range(index):
                if prices[index] - prices[prev_index] > 0:
                    candidates.append(dp[:prev_index + 1] + prices[index] - prices[prev_index])
            dp.append(max(candidates) if candidates else 0)
        return max(dp)
