from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        g = defaultdict(list)
        for a,b,c in edges:
            g[a].append((b,c))
            g[b].append((a,c))
        
        def dfs(a,p,acc):
            ret = int(acc%signalSpeed == 0)
            for b,c in g[a]:
                if b ==p:continue
                ret += dfs(b,a,acc+c)
            return ret 
        N = len(edges) +1
        res = [0]*N
        
        for i in range(N):
            acc =0
            a1 = 0
            for a,c in g[i]:
                b = dfs(a,i,c)
                acc += b*a1 
                a1 += b
            #print(acc,a1)
            res[i] = acc 
        return res
    




re =Solution().countPairsOfConnectableServers(edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], signalSpeed = 1)
print(re)