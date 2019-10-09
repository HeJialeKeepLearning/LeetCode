class Solution:
    def coinChange(self, coins, amount):
        dp = [0]
        count = 1
        while count <= amount:
            sub_amount = [dp[count - each_coin] for each_coin in coins if (count - each_coin >= 0) and (dp[count - each_coin] != -1)]
            if not sub_amount:
                dp.append(-1)
            else:
                dp.append(1 + min(sub_amount))
            count += 1
        return dp[-1]