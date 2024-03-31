from typing import List, Tuple, Optional
# will OT
from functools import cache
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:

        @cache
        def dfs(a,b):
            ret = 0
            for x,y,p in prices:
                if a >=x and b >=y :
                    ret = max(ret,p + dfs(a-x,b) + dfs(x,b-y))
                    ret = max(ret,p + dfs(a,b-y) + dfs(a-x,y))
            return ret
        
        return dfs(m,n)




re = Solution().sellingWood(m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]])
print(re)