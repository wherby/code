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
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        hf = n//2
        @cache 
        def dfs(idx,i,j,pi,pj):
            if i ==j or pi==i or pj ==j :
                return INF
            if idx ==hf:
                return 0
            ret = INF
            acc = cost[idx][i] + cost[n-1-idx][j]
            for i1 in range(3):
                for j1 in range(3):
                    ret = min(ret,acc + dfs(idx+1,i1,j1,i,j))
            return ret
        ans = INF
        for i in range(3):
            for j in range(3):
                ans = min(ans,dfs(0,i,j,-1,-1))
        return ans


re =Solution().minCost(n = 4, cost = [[3,5,7],[6,2,9],[4,8,1],[7,3,5]])
print(re)