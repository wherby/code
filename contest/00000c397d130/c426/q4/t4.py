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
import sys
sys.setrecursionlimit(10000000)

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        

        def getls(edgs,isGood):
            n = len(edgs ) +1
            g= [[] for _ in range(n)]
            for a,b in edgs:
                g[a].append(b)
                g[b].append(a)
            ret = [0]*n
            @cache
            def dfs(a,p,isGood):
                ret = int(isGood)
                for b in g[a]:
                    if b ==p:continue
                    ret += dfs(b,a,not isGood)
                return ret

            for i in range(n):
                ret[i]=dfs(i,-1,isGood)
                #print(i,dfs(i,-1,k))
            dfs.cache_clear()
            return ret
        ls1 = getls(edges1,True)
        ls2 =getls(edges2,False)
        b = max(ls2)
        return [a+b for a in ls1]



re =Solution().maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]])
print(re)