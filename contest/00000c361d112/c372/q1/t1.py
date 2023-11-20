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
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        sm = len(s1)+len(s2) +len(s3)
        n=min(len(s1),len(s2),len(s3))
        for i in range(n,0,-1):
            if s1[:i]==s2[:i] ==s3[:i]:
                return sm - i*3
        return -1





re =Solution()
print(re)