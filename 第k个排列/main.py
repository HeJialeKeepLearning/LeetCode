import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        num_list = [str(i) for i in range(1, n + 1)]
        ret_str = ''
        while k:
            divisor = math.factorial(len(num_list) - 1)
            pick_num = k // divisor
            ret_str += num_list.pop(pick_num)
            k = k % divisor
        ret_str += (''.join(num_list))
        return ret_str