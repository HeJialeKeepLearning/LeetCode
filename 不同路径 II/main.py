import copy

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = copy.deepcopy(obstacleGrid)
        for row in range(0, len(dp)):
            for col in range(0, len(dp[0])):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                elif (row == 0) or (col == 0):
                    if row == 0 and col == 0:
                        dp[row][col] = 1
                    elif row == 0:
                        dp[row][col] = dp[row][col - 1]
                    elif col == 0:
                        dp[row][col] = dp[row - 1][col]
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[-1][-1]