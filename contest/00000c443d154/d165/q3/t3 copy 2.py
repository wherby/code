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
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n <=3:
            return [] 
        ret = []
        ls= [[] for _ in range(n*2)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                ls[(i+j)].append((i,j))
        print(ls)
        return ret


re =Solution().generateSchedule(5)
print(re)