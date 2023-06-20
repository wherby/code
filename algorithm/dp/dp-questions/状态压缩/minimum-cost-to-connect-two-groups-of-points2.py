# https://leetcode.cn/problems/minimum-cost-to-connect-two-groups-of-points/
from typing import List, Tuple, Optional
from collections import defaultdict,deque

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m,n = len(cost),len(cost[0])
        min_cost = [min(col) for col in zip(*cost)]

        def dfs(i,j):
            if i <0:
                return sum(c for k,c in enumerate(min_cost) if j >> k &1)
            return min(dfs(i-1,j & ~ (1<<k)) +c for k,c in enumerate(cost[i]))
        return dfs(n-1,(1<<m)-1)





re =Solution().connectTwoGroups(cost = [[15, 96], [36, 2]])
print(re)