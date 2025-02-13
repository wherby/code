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
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ls = [[] for _ in range(n*2)]
        for i in range(n):
            for j in range(n):
                ls[i-j].append(grid[i][j])
        for i,a in enumerate(ls):
            ls[i] = sorted(a)
        for i in range(n):
            for j in range(n):
                if i <j:
                    grid[i][j] = ls[i-j][i]
                else:
                    grid[i][j] = ls[i-j][-j-1]
        return grid





re =Solution().sortMatrix([[1,7,3],[9,8,2],[4,5,6]])
print(re)