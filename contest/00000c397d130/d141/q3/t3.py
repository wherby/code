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
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        m = len(pattern)
        n = len(source)
        ts = set(targetIndices)
        @cache
        def dfs(i,j):
            if i ==n :
                if j < m:
                    return -10**10
                return 0 
            ret = -10**19
            if i in ts:
                ret =max(ret,dfs(i+1,j)+1)
            if j<m and source[i] == pattern[j]:
                ret = max(ret,dfs(i+1,j+1))
            else:
                ret = max(ret,dfs(i+1,j))
            return ret
        ret = dfs(0,0)
        dfs.cache_clear()
        return ret




re =Solution().maxRemovals(source = "abbaa", pattern = "aba", targetIndices = [0,1,2])
print(re)