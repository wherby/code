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
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        g = [[] for _ in range(n)]
        ind =[0]*n
        for a,b in edges:
            g[b].append(a)
            ind[a] +=1
        sm = 0 
        cur = n 
        st = []
        for i in range(n):
            if ind[i] ==0:
                heappush(st,(-score[i],i))
        while st:
            print(st)
            c,a  = heappop(st)
            print(c,a)
            sm += -c*cur
            cur -=1
            for b in g[a]:
                ind[b] -=1
                if ind[b] ==0:
                    heappush(st,(-score[b],b))
            
        return sm





re =Solution().maxProfit(n = 3, edges = [[0,2]], score = [60084,34608,25733])
print(re)