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
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n= len(edges) +2
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        dps = [0]*n 
        def dfs(a,p,cur):
            dps[a] = cur
            for b in g[a]:
                if b != p:
                    dfs(b,a,cur +1)
        dfs(1,-1,0)
        mx = max(dps)
        mod = 10**9+7 

        return 0 if mx ==0 else pow(2,mx-1,mod)





re =Solution().assignEdgeWeights( [[1,2]])
print(re)