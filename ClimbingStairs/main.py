class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        f1, f2 = 1, 2
        n -= 3
        while n > 0:
            f1, f2 = f2, f1 + f2
            n -= 1
        return f1 + f2
