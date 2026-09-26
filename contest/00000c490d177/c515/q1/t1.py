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
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        mx = 10000
        ret = -1 
        dx,dy= target
        for i,(x,y,r) in enumerate(drones):
            if abs(x-dx) + abs(y-dy)<=r:
                dd =  abs(x-dx) + abs(y-dy)
                if mx >dd:
                    ret = i 
                    mx = dd 
        return ret 





re =Solution()
print(re)