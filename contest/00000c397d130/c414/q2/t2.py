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
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        n = len(start)
        r = (start[-1] - start[0] + d) //(n-1)
        l  =min(b-a for a,b in pairwise(start))
        
        def verify(mid):
            #ls2 = list(ls)
            for i in range(1,n):
                if ls[i] + d >= ls[i-1]+mid :
                    ls[i] = max(ls[i-1]+mid,ls[i])
                else:
                    return False
            #print(ls,mid,ls2)
            return True

        while l <r: 
            mid =(l+r+1)>>1
            #print(mid,verify(mid))
            ls= list(start)
            if verify(mid):
                l = mid 
            else:
                r = mid-1
        return l 




re =Solution().maxPossibleScore(start = [0,9,2,9], d = 2)
print(re)