class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 or not word2:
            return len(word1) ^ len(word2)
        dp = [[0] * len(word2) for _ in range(len(word1))]
        row_first_flag = False
        col_first_flag = False
        for row_index in range(len(dp)):
            for col_index in range(len(dp[0])):
                if word1[row_index] == word2[col_index]:
                    if row_index == 0 and col_index == 0:
                        dp[row_index][col_index] = 0
                        row_first_flag = True
                        col_first_flag = True
                    elif row_index == 0:
                        if row_first_flag:
                            dp[row_index][col_index] = 1 + dp[row_index][col_index - 1]
                        else:
                            dp[row_index][col_index] = dp[row_index][col_index - 1] - 1
                            row_first_flag = True
                    elif col_index == 0:
                        if col_first_flag:
                            dp[row_index][col_index] = 1 + dp[row_index - 1][col_index]
                        else:
                            dp[row_index][col_index] = dp[row_index - 1][col_index] - 1
                            col_first_flag = True
                    else:
                        dp[row_index][col_index] = dp[row_index - 1][col_index - 1]
                else:
                    if row_index == 0 and col_index == 0:
                        dp[row_index][col_index] = 2
                    elif row_index == 0:
                        dp[row_index][col_index] = 1 + dp[row_index][col_index - 1]
                    elif col_index == 0:
                        dp[row_index][col_index] = 1 + dp[row_index - 1][col_index]
                    else:
                        dp[row_index][col_index] = min(1 + dp[row_index - 1][col_index], 1 + dp[row_index][col_index - 1], 2 + dp[row_index - 1][col_index - 1])
        return dp[-1][-1]
