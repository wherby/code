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
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dic=defaultdict(int)
        for ls in grid:
            for a in ls:
                dic[a] +=1
        a,b = -1,-1
        n =len(grid)
        for i in range(1,n**2):
            if i not in dic:
                b =i 
            elif dic[i] ==2:
                a =i 
        return [a,b]





re =Solution()
print(re)