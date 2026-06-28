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
    def maxDistance(self, moves: str) -> int:
        x,y =0,0
        mx = 0 
        z = 0
        for a in moves:
            if a =="U":
                x +=1
            elif a =="D":
                x -=1
            elif a == "L":
                y +=1
            elif a =="R":
                y -=1
            else:
                z +=1
        return abs(x)+abs(y)+z




re =Solution()
print(re)