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
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        l,r1 = 0,10**13
        ds = d[1] + d[0]
        lcm1 = math.lcm(r[0],r[1])
        def verify(md):
            acc = md -md//lcm1
            mv1 = md -md //r[0]
            mv2 = md-md //r[1]

            return acc >=ds and mv1 >=d[0] and mv2 >=d[1] 
        while l < r1:
            md =(l+r1)>>1
            if verify(md):
                r1 =md 
            else:
                l = md +1
        return l 





re =Solution().minimumTime( d = [3,1], r = [2,3])
print(re)