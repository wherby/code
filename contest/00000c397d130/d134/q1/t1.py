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
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        colors= colors+colors
        acc=0
        for i in range(n):
            if colors[i] != colors[i+1] and  colors[i+1] != colors[i+2]:
                acc +=1
        return acc





re =Solution()
print(re)