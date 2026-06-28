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
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        @cache
        def dfs(a,p):
            res = baseTime[a]
            lss = []
            for b in g[a]:
                if b != p:
                    lss.append(dfs(b,a))
            return res if len(lss)==0 else res + max(lss) *2 - min(lss)
        return dfs(0,-1)





re =Solution()
print(re)