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
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        arr1,arr2 = [[0]*n for _ in range(m)],[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "X":
                    arr1[i][j] =1
                if grid[i][j] == "Y":
                    arr2[i][j] =1
        pre1,pre2= Presum2d(arr1),Presum2d(arr2)
        acc =0 
        for i in range(m):
            for j in range(n):
                if pre1.query(0,0,i,j) == pre2.query(0,0,i,j) and pre1.query(0,0,i,j) >0:
                    acc +=1
        return acc





re =Solution()
print(re)