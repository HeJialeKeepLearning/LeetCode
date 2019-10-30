class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [True] * (len(s) + 1)
        for i in range(1, len(dp)):
            for j in range(i - 1, -1, -1):
                dp[i] = dp[j] and (s[j:i] in wordDict)
                if dp[i]:
                    break
        return dp[-1]
