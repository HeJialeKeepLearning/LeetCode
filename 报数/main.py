class Solution:
    def countAndSay(self, n):
        dp = ['1']
        while len(dp) < n:
            last = dp[-1]
            now = self.calculate_next(last)
            dp.append(now)
        return dp[-1]

    def calculate_next(self, last_str):
        last = list(last_str)
        pre = None
        cnt = 0
        ret_str = ''
        for index in range(len(last)):
            if not pre:
                pre = last[index]
                cnt = 0
            if pre != last[index]:
                ret_str += (str(cnt) + str(pre))
                pre = last[index]
                cnt = 0
            cnt += 1
        ret_str += (str(cnt) + str(pre))
        return ret_str
