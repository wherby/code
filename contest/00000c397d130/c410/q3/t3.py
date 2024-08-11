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
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10**9+7
        n = len(nums)
        
        @cache
        def dfs(i,x):
            if i == n-1:
                return 1
            y = nums[i] -x
            if nums[i+1]<x:
                return 0
            ret = 0
            for c in range(x,nums[i+1]+1):
                if nums[i+1]-c <= y and nums[i+1]-c >=0:
                    ret += dfs(i+1,c)
            return ret
        sm = 0
        for i in range(nums[0]+1):
            sm += dfs(0,i)
        return sm%mod




re =Solution().countOfPairs( [5,5,5,5])
print(re)