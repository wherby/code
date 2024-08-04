from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        sm = 0
        mx = m*n
        acc =0
        
        isForce = True
        for i in range(m):
            for j in range(n):
                if j < n//2 and grid[i][j] != grid[i][n-1-j]:
                    if grid[i][j] == grid[m-1-i][j]:
                        grid[i][n-1-j] = 1-grid[i][n-1-j]
                    elif grid[i][n-1-j] ==grid[m-1-i][n-1-j]:
                        grid[i][j] = 1- grid[i][j]
                    else:
                        grid[i][j] = 1- grid[i][j]
                        isForce =False
                    sm +=1
        
        for a in grid:
            acc += sum(a)
        ls = []
        if m%2 ==1 and n%2 ==1:
            ls.append(grid[m//2][n//2])
        #print(ls,acc)
        if acc %4 ==1:
            if len(ls) and ls[0] == 1:
                sm +=1
            else:
                sm +=3
        if acc%4 ==3:
            if len(ls) and ls[0] ==0:
                sm +=1
            else:
                sm +=3
        if acc%4 ==2:
            sm +=2
        #print(mx)
        return sm




re =Solution().minFlips(grid =[[0,0,1],[1,1,1]])
print(re)