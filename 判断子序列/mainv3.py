class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False
        dp = [0]
        index_s = 0
        for each_char in t:
            if each_char == s[index_s]:
                dp.append(dp[-1] + 1)
                index_s += 1
                if index_s == len(s):
                    return True
        return False