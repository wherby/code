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
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        g= [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        res = [-1]*n

        @cache
        def dfs(a,p):
            cur = good[a] if good[a] else -1

            for b in g[a]:
                if b ==p:continue
                r1 = dfs(b,a)
                if r1 > 0:
                    cur += r1 
            if p ==-1:
                res[a] = cur
            return cur if cur >0 else 0
        
        for i in range(n):
            dfs(i,-1)
        return res





re =Solution().maxSubgraphScore(n = 5, edges = [[1,0],[1,2],[1,3],[3,4]], good = [0,1,0,1,1])
print(re)