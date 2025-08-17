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
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        pls= [0]
        pls2 = [0]
        for p,s in zip(prices,strategy):
            pls.append(pls[-1] + p*s)
            pls2.append(pls2[-1] + p)
        ret = pls[-1]
        n = len(prices)
        for i in range(n-k+1):
            acc = pls[i] + pls[-1] - pls[i+k]
            #print(acc,i,  pls[i+1],pls[i] , pls[-1] , pls[i+k],pls)
            acc += pls2[i+k]- pls2[i+k-k//2]
            ret = max(ret,acc)
        return ret 
        





re =Solution().maxProfit(prices = [5,4,3], strategy = [1,1,0], k = 2)
print(re)