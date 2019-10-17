class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        output = []
        s = list(s)

        def backtrace(cur_str, rest_str_list):

            if not rest_str_list:
                output.append(cur_str)
                return
            if rest_str_list[0] == '0':
                return
            if len(rest_str_list) == 1:
                now_str = cur_str + rest_str_list[0]
                output.append(now_str)
                return
            backtrace(cur_str + ' ' + rest_str_list[0], rest_str_list[1:])
            combine_two = rest_str_list[0] + rest_str_list[1]
            if '10' <= combine_two <= '26':
                backtrace(cur_str + ' ' + combine_two, rest_str_list[2:])

        backtrace('', s)
        return len(output)
