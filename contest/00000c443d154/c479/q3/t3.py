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
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        sl = SortedList([])
        ls = []
        cur = 0
        for i in range(n):
            ls.append(damage[i] + requirement[i] + cur)
            cur += damage[i]
            sl.add(ls[-1])
        acc= 0
        cur = 0
        for i in range(n):
            acc +=bisect_right(sl,hp+cur)
            sl.remove(ls[i])
            cur += damage[i]
        return acc




re =Solution().totalScore(hp = 11, damage = [3,6,7], requirement = [4,2,5])
print(re)