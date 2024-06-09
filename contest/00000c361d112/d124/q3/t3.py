from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def dfs(l,r,tar):
            ret =0
            if l+1 > r:
                return ret
            if nums[l] + nums[l+1] == tar:
                ret = max(ret,dfs(l+2,r,tar)+1)
            if nums[l] + nums[r] == tar:
                ret = max(ret,dfs(l+1,r-1,tar)+1)
            if nums[r] + nums[r-1] == tar:
                ret = max(ret,dfs(l,r-2,tar)+1)
            return ret
        ret = 1 
        ret = max(ret,dfs(2,n-1,nums[0]+nums[1])+1)
        ret = max(ret,dfs(1,n-2,nums[0] + nums[n-1])+1)
        ret = max(ret,dfs(0,n-3,nums[n-2]+nums[n-1])+1)
        return ret





re =Solution().maxOperations([3,2,1,2,3,4])
print(re)