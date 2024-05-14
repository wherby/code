from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        g = [[] for _ in range(n)]
        for a,b,c in edges:
            g[a].append((b,c))
            g[b].append((a,c))
        
        mn1 =[10**20]*n
        st = [(0,0)]
        while st:
            c,a = heapq.heappop(st)
            if c > mn1[a]:
                continue
            mn1[a] = c 
            for b,c1 in g[a]:
                heapq.heappush(st,(c+c1,b))
        mn2 =[10**20]*n
        st = [(0,n-1)]
        while st:
            c,a = heapq.heappop(st)
            if c > mn2[a]:
                continue
            mn2[a] = c 
            for b,c1 in g[a]:
                heapq.heappush(st,(c+c1,b))
        m = len(edges)
        ret = [False]*m 
        for i in range(m):
            a,b,c = edges[i]
            if mn1[a]+mn2[a] == mn1[n-1] and mn1[b]+mn2[b] == mn1[n-1]  and abs(mn1[a]-mn1[b] ) ==c:
                ret[i] = True
        #print(mn1,mn2)
        return ret




re =Solution().findAnswer(n = 4, edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]])
print(re)