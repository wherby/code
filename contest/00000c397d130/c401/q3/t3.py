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
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        acc =rewardValues[-1]
        ls = rewardValues[:-1]
        dp = [0]*acc
        dp[0] =1 
        for a in ls:
            for j in range(a):
                if dp[j] ==1 and j+a <acc:
                    dp[j+a] =1
        for j in range(acc-1,-1,-1):
            if dp[j] ==1:
                return acc + j
            



re =Solution()
print(re)