class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = 0
        for ch1 in num1:
            sub_result = 0
            for ch2 in num2:
                sub_result = sub_result * 10 + (ord(ch2) - ord('0')) * (ord(ch1) - ord('0'))
            result = result * 10 + sub_result
        return str(result)
