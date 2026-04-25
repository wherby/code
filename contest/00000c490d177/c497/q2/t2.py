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
    def internalAngles(self, sides: list[int]) -> list[float]:
        sides.sort()
        if sides[0] + sides[1] <= sides[2]:
            return []
        def calc(a, b, c):
            cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
            cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
            cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
            a1 = math.degrees(math.acos(cos_A))
            b1 = math.degrees(math.acos(cos_B))
            c1 = math.degrees(math.acos(cos_C))

            return [a1,b1,c1]
        ls = calc(sides[0],sides[1],sides[2])
        ls.sort()
        return ls





re =Solution()
print(re)