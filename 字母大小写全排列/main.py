class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ret_list = [""]
        for each_char in S:
            if each_char.isdecimal():
                for index in range(len(ret_list)):
                    ret_list[index] += each_char
            else:
                for index in range(len(ret_list)):
                    ret_list.append(ret_list[index] + each_char.upper())
                    ret_list[index] += each_char.lower()
        return ret_list
