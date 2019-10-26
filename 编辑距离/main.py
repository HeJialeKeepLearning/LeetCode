class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if (not word1) or (not word2):
            return len(word1) ^ len(word2)
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        first_col_same_flag = False
        first_row_same_flag = False
        for row_index in range(1, len(dp)):
            for col_index in range(1, len(dp[0])):
                if word1[row_index - 1] == word2[col_index - 1]:
                    if row_index == 1:
                        if first_row_same_flag:
                            dp[row_index][col_index] = 1 + dp[row_index][col_index - 1]
                        else:
                            dp[row_index][col_index] = dp[row_index][col_index - 1]
                            first_row_same_flag = True
                    elif col_index == 1:
                        if first_col_same_flag:
                            dp[row_index][col_index] = 1 + dp[row_index - 1][col_index]
                        else:
                            dp[row_index][col_index] = dp[row_index - 1][col_index]
                            first_col_same_flag = True
                    else:
                        dp[row_index][col_index] = dp[row_index - 1][col_index - 1]
                else:
                    if row_index == 1:
                        dp[row_index][col_index] = 1 + dp[row_index][col_index - 1]
                    elif col_index == 1:
                        dp[row_index][col_index] = 1 + dp[row_index - 1][col_index]
                    else:
                        dp[row_index][col_index] = 1 + min(dp[row_index - 1][col_index], dp[row_index][col_index - 1],
                                                           dp[row_index - 1][col_index - 1])
        return dp[-1][-1]
