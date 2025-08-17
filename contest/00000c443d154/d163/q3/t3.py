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
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        rg =[[] for _ in range(n)]
        for a,b,c in edges:
            g[a].append((b,c))
            rg[b].append((a,c))
        
        st =[(0,0)]
        visit ={}
        while st:
            cost,idx = heappop(st)
            if idx in visit:
                continue
            if idx == n-1:
                return cost
            visit[idx] = cost
            for b,c in rg[idx]:
                heappush(st,(cost +c*2,b))
            for b,c in g[idx]:
                heappush(st,(cost +c,b))
            #print(visit,st)
        return -1





re =Solution().minCost(n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]])
print(re)