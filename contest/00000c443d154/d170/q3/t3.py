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
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        sm = (n+1)*n//2 
        if  target> sm or target < -sm or(sm-target)%2 ==1 :
            return -1 
        diff = (sm -target)//2
        sl = SortedList([])
        for a in range(1,n+1):
            sl.add(a)
        ret = []
        cad = []
        while diff:
            if diff >= sl[-1]:
                ret.append(-sl[-1])
                diff -= sl[-1]
                sl.pop()
            else:
                cad.append(sl.pop())
        return list(ret + cad[::-1] + sl)






re =Solution().lexSmallestNegatedPerm(3,0)
print(re)