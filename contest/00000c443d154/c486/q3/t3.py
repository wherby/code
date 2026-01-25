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
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        def visit(root):
            dis = [-1]*n 

            def dfs(a,p,cur):
                dis[a] = cur 
                for b in g[a]:
                    if b != p:
                        dfs(b,a,cur+1)
            dfs(root,-1,0)
            return dis 
        dp0 = visit(x)
        dp1 = visit(y)
        dp2 = visit(z)
        cnt = 0 
        for i in range(n):
            x,y,z = dp0[i],dp1[i],dp2[i]
            ls= [x,y,z]
            ls.sort()
            x1,y1,z1 = ls 

            if x1**2+y1**2==z1**2:
                cnt +=1

        return cnt



re =Solution().specialNodes(n = 4, edges = [[0,1],[0,2],[0,3]], x = 1, y = 2, z = 3)
print(re)