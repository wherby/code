# https://leetcode.cn/problems/cherry-pickup-ii/description/?envType=daily-question&envId=2024-05-07

from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        
        @cache
        def dfs(idx,x,y):
            if idx == m :
                return 0
            ret = 0
            if 0<=x<n and 0<=y <n:
                for dx in -1,0,1:
                    for dy in -1,0,1:
                        ret = max(ret,dfs(idx+1,x+dx,y+dy)+ grid[idx][x] + (grid[idx][y] if x != y else 0))
                return ret
            else:
                return -10**10
        return dfs(0,0,n-1)



re = Solution().cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]])
print(re)