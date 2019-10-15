class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for index in range(len(digits) - 1, -1, -1):
            result = digits[index] + carry
            carry = result // 10
            digits[index] = result % 10
        if carry:
            digits.insert(0, carry)
        return digits

