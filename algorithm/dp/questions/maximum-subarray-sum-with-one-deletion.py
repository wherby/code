# https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/
from typing import List, Tuple, Optional


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp0,dp1,mx = arr[0],0,arr[0]
        for i in range(1,len(arr)):
            dp1 = max(dp0, dp1 + arr[i])
            dp0 = max(dp0,0 )+ arr[i]
            mx = max(mx,dp0,dp1)
        return mx
        