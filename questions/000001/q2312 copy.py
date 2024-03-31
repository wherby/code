
from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0]* (n+1) for _ in range(m+1)]
        for a,b,c in prices:
            dp[a][b] = c
        @cache
        def dfs(a,b):
            ret = dp[a][b]
            for x in range(1,a//2 +1):
                ret = max(ret, dfs(a-x,b) + dfs(x,b))
            for y in range(1,b//2+1):
                ret = max(ret,dfs(a,b-y) + dfs(a,y))
            return ret
        return dfs(m,n)




re = Solution().sellingWood(m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]])
print(re)