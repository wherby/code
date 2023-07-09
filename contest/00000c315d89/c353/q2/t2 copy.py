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
        def dfs(idx):
            nonlocal ret 
            if idx == n-1:
                return 0
            ret = -n
            for j in range(idx+1,n):
                if abs(nums[idx] - nums[j])<= target:
                    ret =max(ret ,dfs(j)+1)
            return ret
        ret =dfs(0)
        return ret if ret >0 else -1
        





re =Solution().maximumJumps(nums = [1,3,6,4,1,2], target = 0)
print(re)