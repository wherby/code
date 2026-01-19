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
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        mx = -1 
        ret = []
        x,y = center
        for a,b,q in towers:
            if abs(a-x) + abs(b-y) <=radius:
                if q >mx:
                    mx = q 
                    ret=[[a,b]]
                elif q ==mx:
                    ret.append([a,b])
        if len(ret) ==0:
            return [-1,-1]
        else:
            ret.sort()
            return ret[0]





re =Solution()
print(re)