# https://leetcode.cn/problems/new-21-game/description/?envType=daily-question&envId=2025-08-17
from functools import cache
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        @cache
        def dfs(k1):
            if k1 >=k:
                return int(k1 <=n)
            acc = 0 
            for i in range(1,maxPts+1):
                acc += dfs(k1 + i )/maxPts
            return acc 
        return dfs(0)

print(Solution().new21Game(5710,5070,8516))