# https://leetcode.cn/problems/maximum-walls-destroyed-by-robots/description/?envType=daily-question&envId=2026-04-03
from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        ls = sorted(zip(robots,distance),key = lambda p:p[0])
        robots = [a[0] for a in ls ]
        distance = [a[1] for a in ls]

        walls.sort()
        dp = [0]*2
        lstcheck = [-10**10]*2

        def getNumber(left,right):
            r = bisect_right(walls,right)
            l = bisect_left(walls,left)
            return r-l

        for i in range(n):
            ndp = [0]*2 
            ndp[0] = max( dp[0] + getNumber(max(lstcheck[0],robots[i]-distance[i]),robots[i]),
            dp[1] + getNumber(max(lstcheck[1],robots[i]-distance[i]),robots[i]))
            ndp[1] =max(dp[0],dp[1])+getNumber(robots[i],min(robots[i]+distance[i],robots[i+1]-1 if i<n-1 else 10**20 ))
            dp = ndp 
            lstcheck=[robots[i]+1, min(robots[i]+distance[i]+1,robots[i+1]+1 if i<n-1 else 10**20 )]
        return max(dp)

