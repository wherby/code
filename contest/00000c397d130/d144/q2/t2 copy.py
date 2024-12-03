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
            t1,t2=(y-x+26)%26,(x-y+26)%26 
            print(x,y,t1,t2,nextCost[x],previousCost[y])
            cnt += min(nextCost[x]*t1,previousCost[x]*t2)
        return cnt





re =Solution().shiftDistance(s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print(re)