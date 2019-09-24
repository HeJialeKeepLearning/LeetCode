class Solution:
    def generateParenthesis(self, n):
        if n < 1:
            return []
        n_list = []
        n_list.append([''])
        for i in range(1, n + 1):
            new_list = []
            for j in range(i):
                p_list = n_list[j]
                q_list = n_list[i - 1 - j]
                for p in p_list:
                    for q in q_list:
                        new_item = '(' + p + ')' + q
                        new_list.append(new_item)
            n_list.append(new_list)
        return n_list[-1]
