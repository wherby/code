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
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        hs,vs = horizontalCut,verticalCut
        hs.sort()
        vs.sort()
        hsm,vsm = sum(hs),sum(vs)
        a,b=1,1
        sm =0
        while hsm and vsm:
            if hs[-1] > vs[-1]:
                c = hs.pop()
                sm +=b*c
                a +=1 
                hsm -=c 
            else:
                c = vs.pop()
                sm += a*c 
                b +=1
                vsm -=c 
        if hsm:
            sm += b*hsm 
        if vsm:
            sm += a*vsm 
        return sm
        





re =Solution().minimumCost(7,4,[13,6,12,14,4,7],[14,15,11])
print(re,258)
re =Solution().minimumCost(6,3,[2,3,2,3,1],[1,2])
print(re,28)