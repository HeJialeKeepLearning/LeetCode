class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        last_level = []
        dp = [triangle[0][0]]
        for each_level in triangle:
            if not last_level:
                last_level.extend(each_level)
                continue
            cur_level = each_level[:]
            for index in range(len(cur_level)):
                if index == 0:
                    cur_level[index] += last_level[index]
                elif index == len(cur_level) - 1:
                    cur_level[index] += last_level[index - 1]
                else:
                    cur_level[index] += (min(last_level[index - 1], last_level[index]))
            dp.append(min(cur_level))
            last_level = cur_level
        return dp[-1]
