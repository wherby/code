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
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        n = len(strength)
        @cache
        def dfs(state):
            if state ==(1<<n)-1:
                return 0
            t= bin(state).count("1")
            ct = 1+ t*K
            ret = 10**20
            for i in range(n):
                if (1<<i)&state ==0:
                    ret = min(ret,dfs((1<<i)|state ) + (strength[i] +ct-1 )//ct)
            return ret
        return dfs(0)

re =Solution().findMinimumTime(strength = [3,4,1], K = 1)
print(re)