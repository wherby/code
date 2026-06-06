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
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        mod = 10**9+7
        n = len(parent)
        g = [[] for _ in range(n)]

        for i in range(1,n):
            g[parent[i]].append(i)
        
        dfs_ord = []
        sz = [0]*n 

        def dfs(a):
            dfs_ord.append(a)
            sz[a] =1 
            for b in g[a]:
                dfs(b)
                sz[a] += sz[b]
        dfs(0)

        dp0 = [[0]*k for _ in range(n+1)]
        dp1 = [[0]*k for _ in range(n+1)]
        dp0[n][0] = 1 

        for idx in range(n-1,-1,-1):
            a = dfs_ord[idx]
            v = nums[idx] %k 

            for r in range(k):
                dp0[idx][r] = (dp0[idx+1][r] + dp1[idx+1][r])%mod
                nr = idx + sz[a]
                pr = (r-v)%k 
                dp1[idx][r] = dp0[nr][pr]
        return (dp0[0][0] + dp1[0][0]-1)%mod





re =Solution().countValidSubsets( parent = [-1,0,0,0], nums = [2,1,2,1], k = 3)
print(re)