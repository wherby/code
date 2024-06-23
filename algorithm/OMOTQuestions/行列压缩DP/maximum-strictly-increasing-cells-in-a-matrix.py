# https://leetcode.cn/problems/maximum-strictly-increasing-cells-in-a-matrix/description/?envType=daily-question&envId=2024-06-19

from typing import List, Tuple, Optional
from collections import defaultdict,deque

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m,n = len(mat), len(mat[0])
        dp1,dp2 = [0]*m,[0]*n 
        dic = defaultdict(list)
        for i in range(m):
            for j in range(n):
                dic[mat[i][j]].append((i,j))
        keys = list(dic.keys())
        keys.sort()
        for k in keys:
            dp1d=defaultdict(int)
            dp2d =defaultdict(int)
            for i,j in dic[k]:
                dp1d[i] =max(dp1d[i],  max(dp1[i],dp2[j]) +1)
                dp2d[j] =max(dp2d[j],  max(dp1[i],dp2[j]) +1)
            for m,n in dp1d.items():
                dp1[m] = n 
            for m,n in dp2d.items():
                dp2[m] =n 
        return max(dp1+dp2)
        