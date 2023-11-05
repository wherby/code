from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        g= [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        sm = sum(values)
        def dfs(i,p):
            mn = values[i]
            if len(g[i])>1 or (i==0 and len(g[1])>0):
                acc =0
                for a in g[i]:
                    if a ==p:continue
                    acc += dfs(a,i)
                mn = min(mn,acc)
            return mn
        return sm -dfs(0,-1)
            





re =Solution().maximumScoreAfterOperations([[0,1]],[2,1])
print(re)