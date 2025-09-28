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
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9+7
        m = r-l +1
        idp = [1]*m
        ddp = [1]*m

        for _ in range(n-1):
            nidp =[0]*m 
            nddp =[0]*m
            acc = 0
            for i in range(m):
                nddp[i] = acc 
                acc += idp[i]
            acc =0
            for i in range(m-1,-1,-1):
                nidp[i] = acc 
                acc+=ddp[i]
            idp= [a%mod for a in nidp]
            ddp =[a%mod for a in nddp]
        return (sum(idp) + sum(ddp))%mod
        
        





re =Solution().zigZagArrays(3,1,3)
print(re)