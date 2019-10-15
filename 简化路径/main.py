class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        begin, end = 0, 1
        path_list = list(path)
        while end < len(path_list):
            if path_list[end] == '/' or end == len(path_list) - 1:
                if path_list[end] != '/' and end == len(path_list) - 1:
                    end += 1
                cur_path = ''.join(path_list[begin:end])
                if cur_path in ['/..', '/.', '/']:
                    if cur_path == '/..':
                        if stack:
                            stack.pop()
                else:
                    stack.append(cur_path)
                begin = end
                end += 1
            else:
                end += 1
        if not stack:
            stack = ['/']
        return ''.join(stack)
