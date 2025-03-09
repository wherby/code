from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def minCost(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n ==1:
            return nums[0]
        if n ==0:
            return 0
        @cache
        def dfs(idx,lst):

            ret = 10**10
            t = [lst] + nums[idx:idx+2]
            t.sort(reverse= True)
            
            if len(t)==3:
                ret = min(ret,t[1]+dfs(idx+2,t[0]))
                ret = min(ret,t[0]  +dfs(idx+2,t[-1]))
            else:
                ret = t[0]
            return ret
        return dfs(1,nums[0])





re =Solution().minCost([9])
print(re)