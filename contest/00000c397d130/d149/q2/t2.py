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
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        pls= [0]
        for s,e in zip(startTime,endTime):
            pls.append(pls[-1] + e-s)
        mx = 0 
        for i in range(k-1,n):
            if i == n-1:
                r = eventTime
            else:
                r = startTime[i+1]
            #mx =max(mx,r- pls[i+1])
            if i == k-1:
                l = 0
            else:
                l = endTime[i-k]
            #print(r,l,i,r,)
            mx = max(mx,r-l - (pls[i+1]-pls[i+1-k]))
        return mx 





re =Solution().maxFreeTime(eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5])
print(re)