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
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""
        ret = ["A" for a in caption]
        ret2 = ["A" for a in caption]
        dp = [10**10 for _ in range(n+1)]
        nxt = [-1]*(n+1)
        dp[0] = 0 
        
        
        

        
        return "".join(ret2)





re =Solution().minCostGoodCaption(caption = "mibsej")
print(re)