class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [1]
        s = list(s)
        for index in range(len(s)):
            if len(dp) == 1:
                if s[0] == '0':
                    return 0
                dp.append(1)
                continue
            k1, k2 = 0, 0
            if s[index] != '0':
                k1 = 1
            combine_two = ''.join(s[index - 1:index + 1])
            if '10' <= combine_two <= '26':
                k2 = 1
            dp.append(k1 * dp[-1] + k2 * dp[-2])
            if dp[-2] == 0:
                return 0
        return dp[-1]
