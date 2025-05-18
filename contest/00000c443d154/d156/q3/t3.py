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
import abc
class Solution(abc.ABC):
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        g = [[] for _ in range(n)]
        ind = [0]*n 
        for a,b,c in edges:
            g[a].append((b,c))
            ind[b]+=1
        ls =[0]
        ret = -1
        visit=defaultdict(set)
        def dfs(a):
            nonlocal ret
            #if a in visit:
            if len(ls) >k and ls[-1] - ls[-1-k] < t:
                ret = max(ret,ls[-1] - ls[-1-k])
            for b,c in g[a]:
                ls.append(ls[-1]+c)
                dfs(b)
                ls.pop()
            
            #visit[a] =1
        for i in range(n):
            if ind[i] ==0:
                dfs(i)
        return ret  





re =Solution().maxWeight( n = 3, edges = [[0,1,6],[1,2,8]], k = 1, t = 6)
re =Solution().maxWeight(  n = 3, edges = [[0,1,1],[1,2,2]], k = 2, t = 4)
print(re)
c = Solution()
print(dir(c))
print(c.__class__)
print(dir(Solution))
print(Solution.__mro__)