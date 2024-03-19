from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Presum2d:
    def __init__(self,arr):
        m,n = len(arr),len(arr[0])
        self.pre = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                #print(i,j,m,n)
                self.pre[i+1][j+1] = self.pre[i][j+1] + self.pre[i+1][j] -self.pre[i][j] + arr[i][j]
    
    def query(self,x1,y1,x2,y2):
        a = self.pre[x2+1][y1]
        b = self.pre[x1][y2+1]
        c = self.pre[x1][y1]
        return self.pre[x2+1][y2+1] -a -b +c
    
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        pre = Presum2d(grid)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if pre.query(0,0,i,j) <=k:
                    cnt +=1
        return cnt




re =Solution().countSubmatrices(grid = [[7,6,3],[6,6,1]], k = 18)
print(re)