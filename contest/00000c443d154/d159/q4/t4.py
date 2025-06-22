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
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        qd = defaultdict(list)
        for i,(x,k) in enumerate(queries):
            qd[x].append((i,k))
        
        n = len(par)
        g = [[] for _ in range(n)]
        for i,p in enumerate(par):
            if p >= 0:
                g[p].append(i)
        
        m = len(queries)
        res = [-1] *m

        vss = [0]*n 


        def dfs(a,acc):
            st = set([vals[a]^acc])
            for b in g[a]:
                re =  dfs(b,vals[a]^acc) 
                for c in re:
                    st.add(c)
            if len(qd[a]) > 0:
                ost = sorted(list(st))
                for x,k in qd[a]:
                    if k <= len(ost):
                        res[x] = ost[k-1]
                       # print(a,x,k,ost)
            return st
        dfs(0,0)
        return res


re =Solution().kthSmallest(par = [-1,0,1], vals = [5,2,7], queries = [[0,1],[1,2],[1,3],[2,1]])
print(re)