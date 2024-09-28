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
    def minNumberOfSeconds(self, mountainHeight: int, ws: List[int]) -> int:
        l,r =0,10**20

        def verify(mid):
            sm = 0
            for a in ws:
                t = mid//a*2
                p = int(math.sqrt(t))
                #print(mid,t,(p+2)*(p+1)//2,(p+2)*(p+1)//2 <=t,p)
                if (p+1)*(p) <=t:
                    sm+= p
                else:
                    sm +=max(0, p-1)
            #print(mid,sm)
            return sm >= mountainHeight
        while l <r:
            mid = (l+r)>>1
            if verify(mid):
                r = mid 
            else:
                l = mid +1
            #print(mid,verify(mid),l)
        return l





re =Solution().minNumberOfSeconds( mountainHeight = 5, ws = [1])
print(re)