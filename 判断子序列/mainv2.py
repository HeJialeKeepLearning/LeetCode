class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        output_flag = [False]

        def backtrace(cur_index, cur_string):
            if cur_index == len(s):
                output_flag[0] = True
                return True
            for index in range(len(cur_string)):
                if cur_string[index] == s[cur_index]:
                    search_result = backtrace(cur_index + 1, cur_string[index + 1:])
                    if not search_result:
                        return False

        backtrace(0, t)
        if output_flag[0]:
            return True
