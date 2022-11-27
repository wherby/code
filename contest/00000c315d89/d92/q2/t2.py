from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

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
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        pre = Presum2d(grid)
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                t= pre.query(i,0,i,n-1) + pre.query(0,j,m-1,j)
                re = t -(m+n-t)
                res[i][j] =re
        return res




re =Solution().onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]])
print(re)