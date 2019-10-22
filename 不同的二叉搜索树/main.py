class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]
        for i in range(1, n + 1):
            num_result = 0
            for num in range(1, i + 1):
                left_index = num - 1
                right_index = len(dp) - num
                num_result += (dp[left_index] * dp[right_index])
            dp.append(num_result)
        return dp[-1]
