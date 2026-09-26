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

from itertools import pairwise
class Solution:
    def countRotations(self, s: str, k: int) -> int:
        cnt = 0
        n = len(s)
        for i in range(n):
            t= s[i:]+ s[:i]
            acc = 0 
            for a,b in pairwise(t):
                if a ==b:
                    acc +=1
            if acc ==k:
                cnt +=1
        return cnt 





re =Solution().countRotations("ub",0)
print(re)