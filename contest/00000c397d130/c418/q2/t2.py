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
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]

        for a,b in invocations:
            g[a].append(b)
            rg[b].append(a)
        
        visit ={}
        cand = [k]
        bd={}
        while cand:
            a = cand.pop()
            if a in visit:
                continue
            visit[a] =1
            for b in g[a]:
                bd[(a,b)] =1
                cand.append(b)
        cand = [a for a in visit.keys()]
        visit2={}
        while cand:
            a = cand.pop()
            if a in visit2: continue
            visit2[a] = 1
            for b in rg[a]:
                if (b,a)  not in bd: 
                    return [i for i in range(n)]
                cand.append(b)
        return [i for i in range(n) if i not in visit]
        







re =Solution().remainingMethods(n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]])
print(re)