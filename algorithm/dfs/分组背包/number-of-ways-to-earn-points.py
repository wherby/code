# https://leetcode.cn/contest/weekly-contest-335/problems/number-of-ways-to-earn-points/

from typing import List, Tuple, Optional

from functools import cache


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        n = len(types)
        mod = 10**9+7
        @cache
        def dfs(idx,rem):
            res =0
            if rem ==0:
                return 1
            if rem <0:
                return 0
            if idx ==n:
                return 0
            a,b = types[idx]
            for i in range(a+1):
                res +=dfs(idx+1,rem- i*b)
                res %=mod
            return res
        return dfs(0,target)
    