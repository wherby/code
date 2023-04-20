#  https://leetcode.cn/problems/make-array-strictly-increasing/
from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        m,n = len(arr1),len(arr2)
        @cache
        def dfs(idx1,pres):
            if idx1 == m:
                return 0 
            k = bisect_left(arr2,pres+1)
            res = 10**5
            if k < n :
                res = min(res,dfs(idx1+1,arr2[k]) +1)
            if arr1[idx1] <= pres:
                return res
            else:
                return min(res,dfs(idx1+1,arr1[idx1]))
        res = dfs(0,-1) 
        return res if res != 10**5 else -1