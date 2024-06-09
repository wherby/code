# https://leetcode.cn/problems/cherry-pickup/

from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        @cache
        def dfs(k,i,j):
            if i <0 or j <0 or k<i or k<j or grid[k-i][i] <0 or grid[k-j][j]<0:
                return -10**10
            if k == 0:
                return grid[i][j]
            return max(dfs(k-1,i,j), dfs(k-1,i-1,j),dfs(k-1,i,j-1),dfs(k-1,i-1,j-1)) + grid[k-i][i] +(grid[k-j][j] if i!=j else 0)

        return max( dfs(n*2-2,n-1,n-1),0)