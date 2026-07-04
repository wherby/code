
# https://leetcode.cn/problems/find-the-safest-path-in-a-grid/?envType=daily-question&envId=2026-07-01
# 这个题目如果直接二分的话，会超时，需要在verify的时候剪枝，但是对于DSU对应的二分，更好的方式是采用从大到小遍历验证
from typing import List, Tuple, Optional
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
        if yr !=xr:
            if self.rank[xr] <self.rank[yr]:
                xr,yr =yr,xr
            
            self.p[yr] = xr
            if self.rank[xr] == self.rank[yr]:
                self.rank[xr] += 1
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        g = [[-1]*n for _ in range(m)]
        cand = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==1:
                    g[i][j] = 0 
                    cand.append((i,j))
        cur = 0 
        while cand:
            cur +=1
            tmp = []
            for x,y in cand:
                for nx,ny in (x+1,y),(x,y+1),(x-1,y),(x,y-1):
                    if 0<=nx<m and 0<=ny<n and g[nx][ny] == -1:
                        g[nx][ny] = cur 
                        tmp.append((nx,ny))
            cand = tmp
        dsu = DSU(m*n)
        ls= []
        for i in range(m):
            for j in range(n):
                ls.append((g[i][j],i,j))
        ls.sort(reverse= True)
        if g[0][0] ==0 or g[m-1][n-1]==0:
            return 0
        for d,x,y in ls:
            for nx,ny in (x+1,y),(x,y+1),(x-1,y),(x,y-1):
                if 0<=nx<m and 0<=ny<n and g[nx][ny] >=d:
                    dsu.union(x*n+y, nx*n+ny)
            if dsu.find(0) == dsu.find(m*n-1):
                return d
        