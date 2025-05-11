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
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        g = [[] for _ in range(n)]
        ind = [0]*n 
        for a,b,c in edges:
            g[a].append((b,c))
            ind[b]+=1
        ls =[0]
        ret = -1
        visit=defaultdict(set)
        @cache
        def dfs(a,d, acc):
            nonlocal ret
            if d == k and acc <t:
                ret = max(ret,acc)
            for b,c in g[a]:
                dfs(b,d+1,acc+c)
            #visit[a] =1
        for i in range(n):
            dfs(i,0,0)
        return ret  





re =Solution().maxWeight( n = 3, edges = [[0,1,6],[1,2,8]], k = 1, t = 6)
re =Solution().maxWeight(  n = 3, edges = [[0,1,1],[1,2,2]], k = 2, t = 4)
print(re)