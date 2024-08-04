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
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g= [[] for _ in range(n)]
        for i in range(n-1):
            g[i].append(i+1)
        
        def bfs():
            visit ={}
            cand= [0]
            ret = 0
            while cand:
                tmp =[]
                for a in cand:
                    if a in visit:continue
                    visit[a] =1
                    if a == n-1:
                        return ret
                    for b in g[a]:
                        if b not in visit:
                            tmp.append(b)
                cand =tmp 
                ret +=1
                
        ret =[]
        for a,b in queries:
            g[a].append(b)
            ret.append(bfs())
        return ret





re =Solution().shortestDistanceAfterQueries( n = 5, queries = [[2, 4], [0, 2], [0, 4]])
print(re)