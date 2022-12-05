#  https://leetcode.com/contest/weekly-contest-318/problems/minimum-total-distance-traveled/
from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n= len(robot)
        robot.sort()
        factory.sort()
        ls = []
        for f,i in factory:
            ls = ls + [f]*min(i,n)
        m = len(ls)
        dp = [[10**20] *(m+1) for _ in range(n+1)]
        for i in range(m+1):
            dp[0][i] = 0
        for i in range(1,n+1):
            acc =10**20
            for j in range(1,m+1):
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + abs(robot[i-1] - ls[j-1]),acc)
                acc = min(acc,dp[i][j])
        #print(dp)
        return dp[n][m]
