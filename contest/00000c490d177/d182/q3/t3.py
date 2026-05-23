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
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        target = tuple(target)
        visit = set(tuple(p) for p in points)

        if target in visit:
            return 0
        k = 0 
        while True:
            k += 1 
            newP = set()
            cls = list(visit)
            n = len(cls)
            for i,a in enumerate(cls):
                for j in range(n):
                    b = cls[j]
                    c = ((a[0]+b[0])//2,(a[1]+b[1])//2,(a[2]+b[2])//2)
                    if c == target:
                        return k
                    if c not in visit:
                        newP.add(c)
            if not newP:
                return -1
            visit.update(newP)

                    





re =Solution().minGenerations( points = [[1,2,3]], target = [5,5,5])
print(re)