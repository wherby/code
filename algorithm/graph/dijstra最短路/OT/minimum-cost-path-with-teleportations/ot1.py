# https://leetcode.cn/problems/minimum-cost-path-with-teleportations/submissions/694635715/?envType=daily-question&envId=2026-01-28

from typing import List, Tuple, Optional
from collections import defaultdict,deque
from heapq import heapify,heappop,heappush 
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        dis = defaultdict(lambda:10**10)
        st= [(0,0,0,k)]
        m,n = len(grid),len(grid[0])
        while st:
            cost,i,j,k = heappop(st)
            #print(i,j,k,cost,st)
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
                for x in range(m):
                    for y in range(n):
                        if grid[x][y]<=grid[i][j] and dis[(x,y,k-1)]>cost:
                            dis[(x,y,k-1)] = cost 
                            heappush(st,(cost,x,y,k-1))