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
    def countValidSequences(self, n: int, k: int) -> int:
        mod=10**9+7
        @cache
        def dfs(idx,res,isE):
            if idx == 0:
                return int(isE) and (res ==0)
            ret = 0
            for i in range(1,res-idx +2):
                ret += dfs(idx-1,res -i,isE or (i%2 ==0))
                
            return ret %mod
        res= dfs(k,n,False)
        dfs.cache_clear()
        return res




re =Solution().countValidSequences(5,3)
print(re)