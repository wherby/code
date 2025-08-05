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
    def minTime(self, s: str, order: List[int], k: int) -> int:
        m = len(order)
        n = len(s)
        def verify(mid):
            ls = list(set(order[:mid]))
            ls.sort()
            #print(mid,ls)
            cnt = 0
            ls =[-1]+ls 
            for a,b in pairwise(ls):
                cnt += (b-a)*(n-b)
            #print(mid,cnt)
            return cnt >= k
        l,r = 1, m 
        while l<r:
            mid = (l+r)>>1
            if verify(mid):
                r = mid 
            else:
                l = mid+1
        return l-1 if verify(l) else -1




re =Solution().minTime(s = "abc", order = [1,0,2], k = 2)
print(re)