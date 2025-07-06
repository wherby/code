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
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a,b,s,e in edges:
            g[a].append((b,s,e))
        visit =[10**10]*n
        st = [(0,0)]
        while st:
            cur,a = heappop(st)
            if cur >= visit[a]:
                continue
            visit[a] = cur
            for b,s,e in g[a]:
                if cur >e:continue
                toB= max(cur,s) +1
                if toB < visit[b]:
                    heappush(st,(toB,b))
        #print(visit)
        return visit[n-1] if visit[n-1] != 10**10 else -1
            




re =Solution().minTime(5,[[0,3,7,21],[3,4,13,23],[3,4,2,8],[4,0,24,25],[3,2,23,23],[1,0,13,14],[2,0,24,24],[3,1,9,13],[4,1,12,18],[0,3,23,23]])
print(re)