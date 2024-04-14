from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g =[[] for _ in range(n)]
        for a,b,c in edges:
            g[a].append((b,c))
            g[b].append((a,c))
        ret = [-1]*n
        st = [(0,0)]
        vist ={}
        while st:
            c,a = heapq.heappop(st)
            if a in vist:
                continue
            vist[a] = 1 
            if c <disappear[a]:
                ret[a] =c
            else:
                continue
            for b,c1 in g[a]:
                heapq.heappush(st,(c1+c,b))
        return ret 




re =Solution().minimumTime(n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5])
print(re)