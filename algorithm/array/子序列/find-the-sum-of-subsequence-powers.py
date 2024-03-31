# https://leetcode.cn/contest/biweekly-contest-127/problems/find-the-sum-of-subsequence-powers/
# 子序列
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        mod =10**9+7
        n = len(nums)
        nums.sort()

        @cache
        def dfs(idx,mid,cnt):
            #print(idx,mid,cnt,"dd")
            if cnt ==k and idx<n:
                return mid
            ret =0
            for j in range(idx+1,n):
                ret += dfs(j,min(mid,nums[j]-nums[idx]),cnt+1)
            return ret
        res = 0
        for i in range(n):
            res += dfs(i,10**10,1)
        return res %mod
        
        





re =Solution().sumOfPowers(nums = [1,2,3,4], k = 3)
print(re)