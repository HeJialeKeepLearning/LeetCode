class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0, 0]
        for index in range(1, len(s)):
            if s[index] == ')' and s[index - 1] == '(':
                dp.append(dp[-2] + 2)
            elif s[index] == ')' and s[index - 1] == ')':
                prev_valid_length = dp[-1]
                if index - prev_valid_length - 1 >= 0 and s[index - prev_valid_length - 1] == '(':
                    dp.append(dp[-1] + 2 + dp[len(dp) - prev_valid_length - 2])
                else:
                    dp.append(0)
            else:
                dp.append(0)
        return max(dp)
