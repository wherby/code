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
    def countSequences(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache
        def dfs(i,pre):
            if i==n:
                return pre == k
            acc =dfs(i+1,pre) + dfs(i+1,pre*nums[i]) +dfs(i+1,pre/nums[i])
            return acc
        res= dfs(0,1)
        dfs.cache_clear()   
        return res




re =Solution().countSequences([5,3,5],3)
print(re)