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
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        colors= colors+colors
        state =0
        acc =0
        for i in range(n+k-2):
            if colors[i] != colors[i+1]:
                state +=1
            else:
                state = 0
            if state == k-1:
                state = k-2
                acc+=1
        return acc




re =Solution().numberOfAlternatingGroups(colors = [0,1,0,1,0], k = 3)
print(re)