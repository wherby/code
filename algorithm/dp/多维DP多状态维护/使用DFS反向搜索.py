# https://leetcode.com/contest/weekly-contest-475/problems/maximum-path-score-in-a-grid/

from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid),len(grid[0])
        
        @cache 
        def dfs(i,j,k):
            if i <0 or j <0 or k <0:
                return -10**10
            if i ==0 and j ==0:
                return 0 
            b = grid[i][j]
            if b ==0:
                ret = max(dfs(i-1,j,k), dfs(i,j-1,k))
            else:
                ret =  max(dfs(i-1,j,k-1), dfs(i,j-1,k-1)) + b 
            return ret 
        re =  dfs(m-1,n-1,k) 
        return re if re >=0 else -1
    

re = Solution().maxPathScore(grid = [[0, 1],[2, 0]], k = 1)
print(re)