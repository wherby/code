
from typing import List, Tuple, Optional
from heapq import heapify,heappop,heappush 
class Solution:
    def trapRainWater(self, hm: List[List[int]]) -> int:
        visit ={}
        m,n = len(hm),len(hm[0])
        st = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j ==0 or j ==n-1:
                    heappush(st,(hm[i][j],i,j))
                    visit[(i,j)]=1
        sm =0

        while st:
            h,i,j = heappop(st)
            for ni,nj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=ni<m and 0<=nj<n and (ni,nj) not in visit:
                    sm += max(0,h-hm[ni][nj])
                    heappush(st,(max(hm[ni][nj],h),ni,nj))
                    visit[(ni,nj)] =1
                    #print(sm)
        return sm



re = Solution().trapRainWater(hm = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])
#re = Solution().trapRainWater( [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]])
#re = Solution().trapRainWater(hm = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])
print(re)