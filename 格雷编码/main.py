class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [['0'], ['0', '1']]
        if n < len(dp):
            return [int(each_num) for each_num in dp[n]]
        n -= 1
        while n:
            last_gray = dp[-1]
            new_gray = []
            for each_gray in last_gray:
                new_gray.append('0' + each_gray)
            for each_gray in last_gray[::-1]:
                new_gray.append('1' + each_gray)
            dp.append(new_gray)
            n -= 1
        ret_list = []
        for each_gray in dp[-1]:
            ret_list.append(int(each_gray, 2))
        return ret_list
