# https://leetcode.cn/problems/count-special-trip
# 把状态也编码计入DP
from typing import List, Tuple, Optional
from collections import defaultdict,deque


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9+7 
        sm = 0
        dp = defaultdict(int)

        for a in nums:
            if a %2 ==0:
                sm += dp[(a//2,1)]
            dp[(a,1)] += dp[(a*2,0)]
            dp[(a,0)] +=1
        return sm%mod