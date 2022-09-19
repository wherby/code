from functools import cache


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        end = endPos
        mod = 10**9+7
        @cache
        def dfs(idx,res):
            if abs(idx-end)> res:
                return 0
            if abs(idx-end) ==res:
                return 1
            return (dfs(idx+1,res-1) + dfs(idx-1,res-1))%mod
        return dfs(startPos,k)



re =Solution().numberOfWays(startPos = 1, endPos = 2, k = 3)
print(re)