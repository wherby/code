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

from bisect import bisect_right,bisect_left
class Span:
    def __init__(self):
        self.span = []
        
    def add(self,left,right):
        span = self.span
        # 找最左侧的与[left,right]相交的区间[l,r], r大到一定程度才会相交
        lidx = bisect_left(span,left,key=lambda itv:itv[1])
        # 找最右侧的与[left,right]相交的区间[l,r], l大到一定程度才不相交
        ridx = bisect_right(span,right,key=lambda itv:itv[0])
        
        for i in range(lidx,ridx):
            left = min(left,span[i][0])
            right = max(right, span[i][1])
        span[lidx:ridx] = [(left,right)]
        
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        sp = Span()
        for s,e in meetings:
            sp.add(s,e)
        for s,e in sp.span:
            days -= e-s +1
        return days




re =Solution().countDays(days = 10, meetings = [[5,7],[1,3],[9,10]])
print(re)