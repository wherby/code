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
    def countPermutations(self, com: List[int]) -> int:
        mod = 10**9+7
        n = len(com)
        for i in range(1,n):
            if com[0]>=com[i]:
                return 0 
        acc =1 
        for i in range(1,n):
            acc = acc*i %mod 
        return acc




re =Solution()
print(re)