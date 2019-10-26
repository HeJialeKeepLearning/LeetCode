class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        output = []

        def backtrace(prev_ip, cur_index, remain_string):
            if not remain_string:
                if prev_ip not in output:
                    output.append(prev_ip)
                return
            if 1 * (4 - cur_index) <= len(remain_string[1:]) <= 3 * (4 - cur_index):
                if not prev_ip:
                    cur_ip = remain_string[0]
                else:
                    cur_ip = prev_ip + '.' + remain_string[0]
                backtrace(cur_ip, cur_index + 1, remain_string[1:])
            if 1 * (4 - cur_index) <= len(remain_string[2:]) <= 3 * (4 - cur_index):
                if remain_string[0] == '0':
                    return
                if not prev_ip:
                    cur_ip = remain_string[:2]
                else:
                    cur_ip = prev_ip + '.' + remain_string[:2]
                backtrace(cur_ip, cur_index + 1, remain_string[2:])
            if 1 * (4 - cur_index) <= len(remain_string[3:]) <= 3 * (4 - cur_index):
                if remain_string[0] == '0':
                    return
                if remain_string[:3] > '255':
                    return
                if not prev_ip:
                    cur_ip = remain_string[:3]
                else:
                    cur_ip = prev_ip + '.' + remain_string[:3]
                backtrace(cur_ip, cur_index + 1, remain_string[3:])

        backtrace('', 1, s)
        return output
