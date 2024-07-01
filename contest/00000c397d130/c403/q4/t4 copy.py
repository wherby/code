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

    def minimumArea(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ls1= [sum(a) for a in grid]
        ls2 = [sum(a) for a in zip(*grid)]
        a,b = m,n
        for i in range(m):
            if ls1[i]==0:
                a-=1
            else:
                break
        for i in range(a):
            if ls1[m-1-i]==0:
                a-=1
            else:
                break
        for i in range(n):
            if ls2[i]==0:
                b-=1
            else:
                break
        for i in range(b):
            if ls2[n-1-i]==0:
                b-=1
            else:
                break
        return a*b
    
    def minCut2(self,grid):
        m,n = len(grid),len(grid[0])
        mn = m*n
        for i in range(1,m):
            g1,g2=grid[:i],grid[i:]
            g1t,g2t= self.minimumArea(g1),self.minimumArea(g2)
            if g1t ==0 or g2t ==0:
                continue
            else:
                gc = g1t+g2t
                if gc < mn:
                    mn=gc
        return mn
    
    def getMinCut(self,grid):
        gr = [list(a) for a in zip(*grid)]
        return min(self.minCut2(grid), self.minCut2(gr))
        
    
    def minCut(self,grid):
        m,n = len(grid),len(grid[0])
        gr = [list(a) for a in zip(*grid)]
        res = m*n
        for i in range(1,m):
            g1,g2=grid[:i],grid[i:]
            g1t,g2t= self.minimumArea(g1),self.minimumArea(g2)
            if g1t ==0 or g2t ==0:
                continue
            else:
                ret =self.getMinCut(g1)
                ret2 = self.getMinCut(g2)

                res = min(res,g2t+ ret)

                res = min(res,g1t + ret2)
                #print(res,ret,ret2,i,g1t,g2t,g2)
                
        for i in range(1,n):
            g1,g2=gr[:i],gr[i:]
            g1t,g2t= self.minimumArea(g1),self.minimumArea(g2)
            if g1t ==0 or g2t ==0:
                continue
            else:
                ret =self.getMinCut(g1)
                ret2 = self.getMinCut(g2)

                res = min(res,self.minimumArea(g2)+ ret)

                res = min(res,self.minimumArea(g1) + ret2)
        return res
        
        
        
    def minimumSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        return self.minCut(grid)
        
        
        
        





re =Solution().minCut([[1,0,1,0],[0,1,0,1]])
print(re)