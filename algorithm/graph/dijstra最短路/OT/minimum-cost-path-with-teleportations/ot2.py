

from typing import List, Tuple, Optional
from collections import defaultdict,deque
from heapq import heapify,heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        dis = defaultdict(lambda:10**10)
        st= [(0,0,0,k)]
        m,n = len(grid),len(grid[0])
        sl = [SortedList() for _ in range(k)]
        for d in range(k):
            for i in range(m):
                for j in range(n):
                    sl[d].add((grid[i][j],i,j))
        while st:
            cost,i,j,k = heappop(st)
            #print(i,j,k,cost,st,sl)
            if i ==m-1 and j == n-1:
                #print(st,cost)
                return cost 
            if cost >dis[(i,j,k)]:
                continue
            if i < m-1:
                cost1 = cost +grid[i+1][j]
                if cost1< dis[(i+1,j,k)]:
                    dis[(i+1,j,k)] = cost1
                    heappush(st,(cost1,i+1,j,k))
            if j < n-1:
                cost1 = cost + grid[i][j+1]
                if cost1 <dis[(i,j+1,k)]:
                    dis[(i,j+1,k)] = cost1
                    heappush(st,(cost1,i,j+1,k))
            if k >0 :
                rmd = []
                for v,x,y in sl[k-1]:
                    if v <=grid[i][j]:
                        if dis[(x,y,k-1)]>cost:
                            rmd.append((v,x,y))
                            dis[(x,y,k-1)] = cost
                            heappush(st,(cost,x,y,k-1))
                for a in rmd:
                    sl[k-1].remove(a)

from input import grid,k
re =Solution().minCost(grid = grid, k = k)
print(re)