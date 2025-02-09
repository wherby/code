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
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        startTime = [0]+startTime+[eventTime]
        endTime = [0] + endTime+ [eventTime]
        n = len(startTime)
        sl = SortedList([])
        for i in range(1,n):
            t = startTime[i] - endTime[i-1]
            sl.add((t,startTime[i],endTime[i-1]))
        mx = 0 
        #print(sl)
        for i in range(1,n-1):
            t1 = startTime[i] - endTime[i-1]
            t2 = startTime[i+1] - endTime[i]
            c = endTime[i] - startTime[i]
            sl.remove((t1,startTime[i], endTime[i-1]))
            sl.remove((t2,startTime[i+1],endTime[i]))
            #print(c,sl[-1][0])
            if c <= sl[-1][0]:
                mx = max(mx,startTime[i+1]-endTime[i-1])
            else:
                mx = max(mx,startTime[i+1]-endTime[i-1] -c)
                #print(startTime[i+1],endTime[i-1],c,mx)
            sl.add((t1,startTime[i], endTime[i-1]))
            sl.add((t2,startTime[i+1],endTime[i]))
            #print(sl)
        return mx






re =Solution().maxFreeTime(eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5])
print(re)