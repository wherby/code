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
    def findMin(self,x1,y1,x2,y2):
        t= self.pre.query(x1,y1,x2,y2)
        a,b = x2-x1+1,y2-y1+1
        for xt in range(x1+1,x2+2):
            if self.pre.query(xt,y1,x2,y2) == t:
                a -=1
            else:
                break
        #print(a,b)
        for xt in range(x2-1,x2-a-1,-1):
            if self.pre.query(x1,y1,xt,y2)==t:
                a-=1
            else:
                break
        for yt in range(y1+1,y2+2):
            if self.pre.query(x1,yt,x2,y2) == t:
                b -=1
            else:
                break
        for yt in range(y2-1,y2-b-2,-1):
            if self.pre.query(x1,y1,x2,yt)==t:
                b-=1
            else:
                break
        return a*b    
    def minimumArea(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        self.pre = Presum2d(grid)
        return self.findMin(0,0,m-1,n-1)


re =Solution().minimumArea([[0,0],[0,0]])
print(re)