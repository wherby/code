# https://leetcode.cn/problems/minimum-total-distance-traveled/description/?envType=daily-question&envId=2026-04-14
# 使用资源化工厂的方式
# 利用贪心思维，把问题变成类似LIS 的匹配问题

from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        ls = []
        for a,b in factory:
            for _ in range(b):
                ls.append(a)
        ls.sort()
        n = len(robot)
        m = len(ls)

        @cache 
        def dfs(i,j):
            if i == n:
                return 0 
            if j == m :
                return 10**20
            return min(dfs(i,j+1), dfs(i+1,j+1)+abs(robot[i] - ls[j]))
        ret =  dfs(0,0)
        dfs.cache_clear()
        return ret 


