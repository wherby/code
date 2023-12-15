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
    def findPeaks(self, ms: List[int]) -> List[int]:
        n = len(ms)
        return [i for i,a in range(1,n-1) if ms[i]>ms[i-1] and ms[i]> ms[i+1] ]





re =Solution()
print(re)