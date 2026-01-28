

from typing import List, Tuple, Optional
from collections import defaultdict,deque
from heapq import heapify,heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        dis = defaultdict(lambda:10**10)
        
        m,n = len(grid),len(grid[0])
        st = [(0,0,0)]
        while st:
            cost,i,j = heappop(st)
            if cost >dis[(i,j)]:
                continue
            if i < m-1:
                cost1 = cost +grid[i+1][j]
                if cost1< dis[(i+1,j)]:
                    dis[(i+1,j)] = cost1
                    heappush(st,(cost1,i+1,j))
            if j < n-1:
                cost1 = cost + grid[i][j+1]
                if cost1 <dis[(i,j+1)]:
                    dis[(i,j+1)] = cost1
                    heappush(st,(cost1,i,j+1))

        for _ in range(k):
            st= [(0,0,0)]
            sl = SortedList()
            for i in range(m):
                for j in range(n):
                    sl.add((grid[i][j],i,j))
            while st:
                cost,i,j = heappop(st)
                if cost >dis[(i,j)]:
                    continue
                if i < m-1:
                    cost1 = cost +grid[i+1][j]
                    if cost1< dis[(i+1,j,k)]:
                        dis[(i+1,j,k)] = cost1
                        heappush(st,(cost1,i+1,j))
                if j < n-1:
                    cost1 = cost + grid[i][j+1]
                    if cost1 <dis[(i,j+1,k)]:
                        dis[(i,j+1,k)] = cost1
                        heappush(st,(cost1,i,j+1))
                if k >0 :
                    rmd = []
                    for v,x,y in sl:
                        if v <=grid[i][j]:
                            if dis[(x,y)]>cost:
                                rmd.append((v,x,y))
                                dis[(x,y)] = cost
                                heappush(st,(cost,x,y))
                    for a in rmd:
                        sl.remove(a)
        return dis[(m-1,n-1)]

from input import grid,k
re =Solution().minCost(grid = grid, k = k)
re =Solution().minCost(grid = [[3,5],[5,7]], k = 0)
print(re)