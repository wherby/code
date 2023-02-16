from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m,n = len(grid),len(grid[0])
        g = [[] for _ in range(m*n)]
        #print(len(g),m,n)
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(m):
            for j in range(n):
                for dx,dy  in dir:
                    nx,ny = dx+i,dy+j
                    if nx < m and ny <n:
                        if grid[i][j] ==1 and grid[nx][ny] == 1:
                            g[i*n + j].append(nx *n +ny)
                            g[nx*n+ ny].append(i*n+j)
        dic = defaultdict(list)
        def dfs(x,y,idx):
            if idx in dic[(x,y)]:
                return
            dic[(x,y)].append(idx)
            for i in range(4):
                #print(dir[i])
                dx,dy = tuple(dir[i])
                nx,ny = dx+x,dy+y
                if nx < m and ny <n and nx>=0 and ny>=0:
                    if grid[x][y] ==1 and grid[nx][ny] == 1 and i not in dic[(nx,ny)]:
                        dfs(nx,ny,i)
        dfs(0,0,-1)
        #print(dic)
        if (m==1 and n ==2) or (m==2 and n==1):
            return False
        return len(dic[(m-1,n-1)])<=1



re =Solution().isPossibleToCutPath(grid =[[1,1]])
print(re)