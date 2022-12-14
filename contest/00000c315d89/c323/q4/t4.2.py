from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from collections import defaultdict,deque
from collections import defaultdict,deque
class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        xr = self.find(x)
        yr = self.find(y)
        if self.rank[xr] <self.rank[yr]:
            xr,yr =yr,xr
        
        self.p[yr] = xr
        self.rank[xr] += self.rank[yr]

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        qls= []
        for i,a in enumerate(queries):
            qls.append((a,i))
        qls.sort()
        m,n = len(grid),len(grid[0])
        st =[]
        for i in range(m):
            for j in range(n):
                heapq.heappush(st,(grid[i][j],i,j))
        dsu=DSU(m*n)
        ans = [0]*len(queries)
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        visit={}
        for q,idx in qls:
            while st and st[0][0]<q:
                a,x,y = heapq.heappop(st)
                for dx,dy in dir:
                    nx,ny = x+dx,y+dy 
                    if 0<=nx<m and 0<=ny<n and (nx,ny) in visit :
                        if dsu.find(x *n +y) != dsu.find(nx*n +ny):
                            dsu.union(x *n +y, nx*n +ny)
                visit[(x,y)] =1
            if (0,0) in visit:
                ans[idx] = dsu.rank[dsu.find(0)]
            #print(q,idx,visit)
        return ans
                
        




re =Solution().maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2])
print(re)