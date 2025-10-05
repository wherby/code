
from typing import List, Tuple, Optional
from heapq import heapify,heappop,heappush 

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
    def trapRainWater(self, hm: List[List[int]]) -> int:
        visit ={}
        m,n = len(hm),len(hm[0])
        st = []
        for i in range(m):
            for j in range(n):
                heappush(st,(hm[i][j],i,j))
        sm =0
        dsu =DSU(m*n)
        while st:
            h,i,j = heappop(st)
            


re = Solution().trapRainWater(hm = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])
#re = Solution().trapRainWater( [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]])
print(re)