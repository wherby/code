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
    def minRotations(self, n: int, s: str) -> int:

        def dist(a, b):
            a, b = int(a), int(b)
            d = abs(a - b)
            return min(d, 10 - d)
        total = 0
        prev = 0
        for ch in s:
            total += dist(prev, ch)
            prev = ch
        
        ans = total 
        
        for k in range(n):
            if k == 0:
                old_conn = dist(0, s[0])
                new_conn = dist(0, s[-1])
            else:
                old_conn = dist(s[k-1], s[k])
                new_conn = dist(s[k-1], s[-1])
            delta = new_conn - old_conn
            ans = min(ans, total + delta)
        
        return ans





re =Solution().minRotations( n = 3, s = "269")
print(re)