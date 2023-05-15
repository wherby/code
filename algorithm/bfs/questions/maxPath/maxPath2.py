# https://leetcode.cn/contest/weekly-contest-345/problems/maximum-number-of-moves-in-a-grid/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n  = len(grid),len(grid[0])
        
        @cache
        def dfs(i,j):
            mx = 0
            for a,b in (i-1,j+1),(i,j+1),(i+1,j+1):
                if 0<=a<m and 0<=b<n and grid[a][b] > grid[i][j]:
                    mx = max(mx, 1+dfs(a,b))
            return mx
        ret =0
        for i in range(m):
            ret =max(ret,dfs(i,0))
        return ret