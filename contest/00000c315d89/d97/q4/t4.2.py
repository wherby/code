from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m,n = len(grid),len(grid[0])
        isFind = False
        dir = [[1,0],[0,1]]
        def dfs(x,y):
            nonlocal isFind
            if isFind == True:return
            if x == m-1 and y == n-1:
                isFind =True
                return
            grid[x][y]=0
            for dx,dy in dir:
                nx,ny = x+dx,y+dy 
                if nx <m and ny<n and grid[nx][ny] ==1:
                    dfs(nx,ny)
        dfs(0,0)
        #print(grid)
        isFind = False
        dfs(0,0)
        return not isFind



#re =Solution().isPossibleToCutPath(grid =[[1,1]])
re =Solution().isPossibleToCutPath([[1,1,1],[1,0,1],[1,1,1]])
print(re)