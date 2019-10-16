class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret_list = []
        def backtrace(first, cur):
            if len(cur) == k:
                ret_list.append(cur[:])
                return
            for i in range(first, n + 1):
                cur.append(i)
                backtrace(i + 1, cur)
                cur.pop()
        backtrace(1, [])
        return ret_list
