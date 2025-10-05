# https://leetcode.cn/problems/trapping-rain-water-ii/solutions/2998212/duan-ban-xiao-ying-pythonjavacgojsrust-b-39mp/?envType=daily-question&envId=2025-10-03
# 通过对边界取最小值，使得二维图形变成一维的计算，不断更新临接点“水位”的最大值，然后找到当前水位最小值计算

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