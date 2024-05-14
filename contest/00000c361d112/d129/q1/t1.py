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
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        def getV(c):
            if c == "W":
                return 1 
            return 0
        for i in range(2):
            for j in range(2):
                acc =0 
                for m,n in (i,j),(i,j+1),(i+1,j),(i+1,j+1): 
                    acc +=getV(grid[m][n])
                if acc != 2 :
                    return True
                #print(acc,i,j)
        return False





re =Solution().canMakeSquare([["B","W","B"],["B","W","W"],["B","B","B"]])
print(re)