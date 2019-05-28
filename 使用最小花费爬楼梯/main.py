class Solution:
    def minCostClimbingStairs(self, cost):
        f = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            f.append(min(f[i - 1], f[i - 2]) + cost[i])
        return min(f[-1],f[-2])
