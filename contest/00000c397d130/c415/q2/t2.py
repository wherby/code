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
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp=[-10**10]*5
        dp[0] = 0
        for c in b:
            for j in range(4,0,-1):
                dp[j] = max(dp[j],dp[j-1]+ a[j-1]*c)
        return dp[-1]



re =Solution().maxScore(a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7])
print(re)