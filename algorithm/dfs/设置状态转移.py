# https://leetcode.cn/problems/max-dot-product-of-two-subsequences/submissions/689890510/?envType=daily-question&envId=2026-01-08
from typing import List, Tuple, Optional
from functools import cache




class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m,n = len(nums1),len(nums2)
        @cache
        def dfs(i,j):
            if i < 0 or j<0:
                return -10**20
            ret = nums1[i]*nums2[j] + max(dfs(i-1,j-1),0)
            ret = max(ret,dfs(i-1,j),dfs(i,j-1))
            return ret 
        return dfs(m-1,n-1)