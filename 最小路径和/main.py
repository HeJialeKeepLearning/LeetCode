class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = grid
        for row in range(len(dp)):
            for col in range(len(dp[0])):
                if row == 0 or col == 0:
                    if row == 0 and col == 0:
                        continue
                    elif row == 0:
                        dp[row][col] += dp[row][col - 1]
                    elif col == 0:
                        dp[row][col] += dp[row - 1][col]
                else:
                    dp[row][col] += min(dp[row - 1][col], dp[row][col - 1])
        return dp[-1][-1]