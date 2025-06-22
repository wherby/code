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
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        cnt = 0
        def dfs(a,p,cur):
            nonlocal cnt
            c = cur+ cost[a]
            cd = []
            for b in g[a]:
                if b ==p:continue
                cd.append(dfs(b,a,c))
            if len(cd) ==0:
                return c 
            mx = max(cd)
            for a in cd :
                if a != mx:
                    cnt +=1
                    print(cd,a,p)
            return mx
        dfs(0,-1,0)
        return cnt





re =Solution().minIncrease(5,[[0,1],[1,2],[0,3],[3,4]],[2,22,3,4,21])
print(re)