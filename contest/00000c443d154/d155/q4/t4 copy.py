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
            g[a].append(b)
            ind[b] +=1

        root = []
        for i in range(n):
            if ind[i] ==0:
                root.append(i)
        sm = 0
        px = [-1]*n
        
        def dfs(a):
            acc = [score[a]]
            for b in g[a]:
                acc.extend(dfs(b))
            px[a]=sum(acc)/(len(acc))
            return acc

        for a in root:
            dfs(a)
        st = []
        for a in root:
            heappush(st,(px[a],a))
        cur =1
        print(px)
        while st:
            _,a = heappop(st)
            sm += score[a]*cur 
            cur +=1
            for b in g[a]:
                ind[b] -=1
                if ind[b] ==0:
                    heappush(st,(px[b],b))
        return sm





re =Solution().maxProfit(n = 3, edges = [[0,2]], score = [60084,34608,25733])
re =Solution().maxProfit(n = 4, edges = [[1,2]], score = [60098,57669,86595,58482])
print(re)