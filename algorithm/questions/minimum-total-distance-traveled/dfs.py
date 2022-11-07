# https://leetcode.cn/contest/weekly-contest-318/problems/minimum-total-distance-traveled/
from typing import List
from functools import cache
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        m,n = len(robot),len(factory)
        @cache
        def dfs(idx,fidx,cnt):
            if idx == m: return 0
            if fidx == n:return 10**20
            if cnt == factory[fidx][1]:return dfs(idx,fidx+1,0)
            cst = abs(factory[fidx][0]- robot[idx]) + dfs(idx +1,fidx,cnt +1)
            cst = min(cst,dfs(idx,fidx+1,0))
            return cst
        return dfs(0,0,0)