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
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        m,n= len(series1),len(series2)
        series1.append([10**10,0])
        series2.append([10**10,0])
        cur1,cur2 = 0,0
        ret =[]
        while cur1 <m or cur2 < n:
            t1=min(series1[cur1][0],series2[cur2][0])
            s1 = series1[cur1][1] + series2[cur2][1]
            ret.append([t1,s1])
            if t1 ==series1[cur1][0]:
                cur1 +=1
            if t1 == series2[cur2][0]:
                cur2 +=1
        return ret





re =Solution()
print(re)