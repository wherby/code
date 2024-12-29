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
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        sm = 0
        for i in range(n):
            cur = grid[0][i]
            for j in range(m):
                sm += max(0,cur- grid[j][i])
                cur = max(cur, grid[j][i])+1
            #print(i,sm,cur)
        return sm






re =Solution().minimumOperations([[3,2],[1,3],[3,4],[0,1]])
print(re)