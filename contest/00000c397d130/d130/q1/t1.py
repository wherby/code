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
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if i != m-1 and grid[i][j] != grid[i+1][j]:
                    return False
                if j != n-1 and grid[i][j] == grid[i][j+1]:
                    return False
        return True





re =Solution()
print(re)