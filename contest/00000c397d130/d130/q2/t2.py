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
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        dic =defaultdict(list)
        for (x,y), a in zip(points,s):
            dic[a].append(max(abs(x),abs(y)))
        mn = 10**39
        for k,v in dic.items():
            if len(v)>=2:
                v.sort()
                mn = min(mn,v[1])
        sm = 0
        #print(mn)
        for k,v in dic.items():
            v.sort()
            for i in range(min(2,len(v))):
                if v[i]<mn:
                    sm +=1
                    #print(v[i],k)
        return sm





re =Solution().maxPointsInsideSquare([[-1,-4],[16,-8],[13,-3],[-12,0]],"abda")
print(re)