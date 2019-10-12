class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ')
        str_list = s.split(' ')
        return len(str_list[-1])