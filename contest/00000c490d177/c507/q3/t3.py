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
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        g = [[] for _ in range(n)]
        for a,b,w in edges:
            g[a].append((b,w))
        visit =defaultdict(lambda : 10**20)
        st = [(0,0,1)]
        while st:
            cost,idx,acc = heappop(st)
            if visit[(idx,acc)]<=cost:
                continue
            if idx == n-1:

                return cost
            visit[(idx,acc)] = cost
            for b,w in g[idx]:
                if labels[b] != labels[idx]:
                    heappush(st,(cost+w,b,1))
                elif acc + 1 <=k:
                    heappush(st,(cost+w,b,acc+1))

        return -1
                





re =Solution().shortestPath(n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2)
print(re)