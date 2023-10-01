from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        cnt = 0
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        def dfs(v,p):
            nonlocal cnt
            ret = values[v]
            # if ret %k ==0:
            #     cnt +=1
            for b in g[v]:
                if b ==p:continue
                ret += dfs(b,v)
                # if ret %k ==0:
                #     cnt +=1
            if ret %k ==0:
                cnt +=1
            return ret %k
        dfs(0,-1)
        return cnt





re =Solution().maxKDivisibleComponents(n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3)
print(re)