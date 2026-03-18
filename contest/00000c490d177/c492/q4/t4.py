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
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        n = len(s)
        pre = [0]
        for i in range(n):
            pre.append(pre[-1]+(1 if s[i] == "1" else 0))
        @cache
        def dfs(l,r):
            x = pre[r+1]-pre[l]
            res = 10**20
            L = r-l+1
            if x ==0:
                res = flatCost
            else:
                res = encCost*x*L
            if L %2 ==0:
                mid = l + L//2
                res = min(res,dfs(l,mid-1)+dfs(mid,r))
            return res
        res =dfs(0,n-1)
        dfs.cache_clear()
        return res




re =Solution()
print(re)