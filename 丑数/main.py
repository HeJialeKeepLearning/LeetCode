class Solution:
    def isUgly(self, num):
        if num <= 0:
            return False
        denominator_list = [2, 3, 5]
        for denominator in denominator_list:
            while not num % denominator:
                num /= denominator
        return num == 1
