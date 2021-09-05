#https://leetcode.com/contest/weekly-contest-63/problems/min-cost-climbing-stairs/
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [float("inf")] *(n+1)
        dpn =[float("inf")] *(n+1)
        dp[0] = dpn[0] =0
        for i in range(1,n+1):
            dp[i] =min(dp[i-1] + cost[i-1], dpn[i-1]+cost[i-1])
            dpn[i] =dp[i-1]
        return min(dp[n],dpn[n])

s=Solution()
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
s.minCostClimbingStairs(cost)

