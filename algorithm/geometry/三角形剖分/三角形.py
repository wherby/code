# https://leetcode.cn/problems/minimum-score-triangulation-of-polygon/description/?envType=daily-question&envId=2025-09-29
# 多边形剖分三角形，每条边都是三角形的一个边，所以可以用首尾作为边作为一个边遍历分割

from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        @cache
        def dfs(i,j):
            if i+1>=j:
                return 0 
            ret = 10**20
            for k in range(i+1,j):
                ret = min(ret, dfs(i,k)+dfs(k,j) + values[i]*values[j]*values[k])
            return ret 
        return dfs(0,n-1)