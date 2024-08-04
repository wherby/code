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
        for a in grid:
            acc += sum(a)
        
        for i in range(m):
            for j in range(n):
                if j<n//2 and grid[i][j] != grid[i][n-1-j]:
                    sm +=1
        #print(sm)
        if sm >0 and (acc+sm)%4==1 or (acc+sm)%4 ==3:
            if n%2  ==1:
                sm +=1
            else:
                sm += m*n
        elif sm ==0 and acc%4 != 0:
            if acc%4 ==2:
                sm +=2
            elif n%2 ==0:
                sm +=1
            else:
                sm += m*n
        mx = min(mx,sm)
        sm = 0
        #print(mx)
        for i in range(m):
            for j in range(n):
                if i<m//2 and grid[i][j] != grid[m-1-i][j]:
                    sm +=1
        print(sm,(acc+sm)%4)
        if sm >0 and (acc+sm)%4==1 or (acc+sm)%4 ==3:
            if m %2 ==0:
                sm +=1
            else:
                sm += m*n
        elif sm ==0 and acc%4 != 0:
            if acc%4 ==2:
                sm +=2
            elif m%2 ==0:
                sm +=1
            else:
                sm += m*n
        mx =min(mx,sm)
        #print(mx)
        return mx




re =Solution().minFlips(grid =[[0,0,1],[1,1,0],[1,1,1],[0,1,1]])
print(re)