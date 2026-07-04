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
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        ls = []
        occupiedIntervals.sort()
        curS = occupiedIntervals[0][0]
        curE = occupiedIntervals[0][1]+1
        for s,e in occupiedIntervals:
            if s > curE:
                ls.append([curS,curE-1]) 
                curS = s 
                curE = e+1
            else:
                curE= max(curE,e +1)
        ls.append([curS,curE-1])
        ret = []
        for s,e in ls:
            if e <freeStart or s>freeEnd:
                ret.append([s,e])
            elif freeStart<= s and e <= freeEnd:
                continue
            elif s<freeStart and e>=freeStart:
                ret.append([s,freeStart-1])
            elif s< freeStart and e >





re =Solution().filterOccupiedIntervals(occupiedIntervals = [[2,6],[4,8],[10,10],[10,12],[14,16]], freeStart = 7, freeEnd = 11)
print(re)