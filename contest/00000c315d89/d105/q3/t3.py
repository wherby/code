from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        mx =min(nums)
        n = len(nums)
        
        def dfs(idx,acc,ls):
            nonlocal mx
            if idx == n:
                if len(ls)>0:
                    mx = max(mx,acc)
                return 
            dfs(idx+1,acc,ls)
            tls =ls + [nums[idx]]
            dfs(idx+1,acc*nums[idx],tls)
        dfs(0,1,[])
        return mx 
            





re =Solution().maxStrength(nums = [0,-1])
print(re)