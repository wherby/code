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
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        cnt = 0
        for i,(a,b) in enumerate(zip(s,t)):
            x,y = ord(a)-ord('a'),ord(b)-ord('a')
            x1=x
            t1,t2= 0,0 
            while x1!= y:
                t1 += nextCost[x1]
                x1 = (x1+1 +26)%26
            x1 = x
            while  x1 != y:
                t2 += previousCost[x1]
                x1 = (x1-1 +26)%26
            cnt += min(t1,t2)
        return cnt





re =Solution().shiftDistance(s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print(re)