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
    def countEffective(self, nums: List[int]) -> int:
        mod = 10**9+7
        sm = 0 
        for a in nums:
            sm = sm| a 
        n = len(nums)
        #print(sm)
        @cache
        def dfs(idx,st):
            if idx ==n:
                return 1 
            ret = dfs(idx+1,st)
            if st|nums[idx] < sm:
                ret += dfs(idx+1,st|nums[idx])
            return ret %mod
        return dfs(0,0)  



re =Solution().countEffective([1,2,3])
print(re)