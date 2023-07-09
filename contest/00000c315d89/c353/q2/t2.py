from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        ret = -1
        n = len(nums)
        
        @cache
        def dfs(idx,sn):
            #print(idx,sn)
            nonlocal ret 
            if idx == n-1:
                ret = max(ret,sn)
            for j in range(idx+1,n):
                if abs(nums[idx] - nums[j])<= target:
                    dfs(j,sn+1)
        dfs(0,0)
        return ret
        





re =Solution().maximumJumps(nums = [1,3,6,4,1,2], target = 2)
print(re)