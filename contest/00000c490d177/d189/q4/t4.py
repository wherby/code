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
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        allP = sorted(set([start] + requests))
        N = len(allP)
        
        startIdx = allP.index(start)
        
        @cache
        def dp(i,j,idx):
            if i ==0 and j ==N-1:
                return 0
            p =j if idx else i 
            ret =10**30
            rem = N-(j-i+1)
            if i >0:
                dis = allP[p] -allP[i-1]
                ret = min(ret,dp(i-1,j,0)+dis*rem)
            if j < N-1:
                dis= allP[j+1] -allP[p]
                ret = min(ret,dp(i,j+1,1)+dis*rem)
            return ret 
        res = dp(startIdx,startIdx,0)
        dp.cache_clear()
        return res





re =Solution()
print(re)