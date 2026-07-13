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
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        ls1 = startTime.split(":")
        ls2 = endTime.split(":")
        acc =0
        for i,(a,b) in enumerate(ls2,ls1):
            a,b = int(a),int(b)
            acc +=(a-b)*(60**(2-i))
        return acc




re =Solution()
print(re)