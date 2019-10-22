class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        dp = [[0] * (len(matrix[0]) + 1)]
        for row in matrix:
            new_line = [0]
            dp.append(new_line)
            for col in row:
                new_line.append(int(col))
        max_area = 0
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                if dp[row][col] and dp[row - 1][col] and dp[row][col - 1] and dp[row - 1][col - 1]:
                    dp[row][col] = 1 + min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1])
                    max_area = max(pow(dp[row][col], 2), max_area)
                else:
                    max_area = max(dp[row][col], max_area)
        return max_area
