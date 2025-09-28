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
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9+7
        
        @cache
        def dfs(idx,i,c):
            if idx == n-1:
                return 1
            ret = 0
            if c:
                for ni in range(i+1,r+1):
                    ret +=dfs(idx+1,ni,False)
            else:
                for ni in range(l,i):
                    ret += dfs(idx+1,ni,True)
            return ret%mod 
        sm = 0
        for i in range(l,r+1):
            sm+= dfs(0,i,True)
            sm+= dfs(0,i,False)
        return sm%mod
        





re =Solution().zigZagArrays(3,1,3)
print(re)