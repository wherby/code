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
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        
        

        def getls(edgs,k):
            n = len(edgs ) +1
            g= [[] for _ in range(n)]
            for a,b in edgs:
                g[a].append(b)
                g[b].append(a)
            ret = [0]*n
            @cache
            def dfs(a,p,k1):
                if k1<0:
                    return 0
                ret = 1 
                for b in g[a]:
                    if b == p:continue
                    ret += dfs(b,a,k1-1)
                return ret

            for i in range(n):
                ret[i]=dfs(i,-1,k)
                #print(i,dfs(i,-1,k))
            dfs.cache_clear()
            return ret
        ls1 =getls(edges1,k)
        ls2 = getls(edges2,k-1)
        b = max(ls2)
        return [a+b for a in ls1 ]


re =Solution().maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2)
print(re)