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
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        MX= max(max(i[0],i[1]) for i in items)+1
        ls= [0]*MX

        for f,p in items:
            ls[f] +=1
        for i in range(1,MX):
            cur = 0 
            for j in range(i,MX,i):
                cur+= ls[j]
            ls[i] = cur 
        dp = [0]*(budget+1)
        mnp = min(i[1] for i in items)
        for f,p in items:
            for j in range(budget,p-1,-1):
                dp[j] =max(dp[j],dp[j-p] + ls[f])
        ret = 0 
        for i in range(mnp,budget+1):
            ret =max(ret, dp[i] + (budget-i) // mnp )
        return ret






re =Solution().maximumSaleItems( items = [[6,2],[2,6],[3,4]], budget = 9)
print(re)