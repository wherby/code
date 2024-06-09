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
                #print(idx,mid,cnt,"AA",n-idx)
                return 1
            ret =0
            for j in range(idx+1,n):
                if nums[j]-nums[idx]>=mid:
                    ret +=dfs(j,mid,cnt +1)
            return ret
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                res += dfs(j,nums[j]-nums[i],2)*(nums[j]-nums[i])
                if  dfs(j,nums[j]-nums[i],2):
                    print(j,i,dfs(j,nums[j]-nums[i],2))
        return res %mod
        
        





re =Solution().sumOfPowers(nums = [1,2,3,4], k = 3)
print(re)