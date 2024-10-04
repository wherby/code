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
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        acc =0
        for c in commands:
            if c =="UP":
                acc -= n
            if c =="RIGHT":
                acc +=1
            if c=="DOWN":
                acc +=n  
            if c=="LEFT":
                acc -=1
        return acc





re =Solution()
print(re)