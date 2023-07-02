# https://leetcode.cn/problems/minimum-cost-to-connect-two-groups-of-points/
from typing import List, Tuple, Optional
from collections import defaultdict,deque

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m,n = len(cost),len(cost[0])
        dp = [[10**10]*(1<<n) for _ in range(m+1)]
        dp[0][0] = 0 
        for i in range(1,m+1): ## 表示从 00001 =》11111
            for j in range(1<<n):
                for k in range(n):
                    if (1<<k) & j :
                        c = cost[i-1][k]
                        j1 = j -(1<<k)
                        dp[i][j] = min(dp[i][j], dp[i-1][j]+ c ,dp[i][j1] + c, dp[i-1][j1] +c)
        return dp[m][(1<<n)-1]





re =Solution().connectTwoGroups(cost = [[15, 96], [36, 2]])
print(re)