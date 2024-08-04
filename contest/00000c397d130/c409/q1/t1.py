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

class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.dic=defaultdict(int)
        n = len(grid)
        self.rdic ={}
        for i in range(n):
            for j in range(n):
                self.dic[(i,j)] = grid[i][j]
                self.rdic[grid[i][j]]=(i,j)

    def adjacentSum(self, value: int) -> int:
        sm = 0
        x,y = self.rdic[value]
        for nx,ny in (x,y+1),(x+1,y),(x,y-1),(x-1,y):
            sm += self.dic[(nx,ny)]
        return sm
        


    def diagonalSum(self, value: int) -> int:
        sm = 0
        x,y = self.rdic[value]
        for nx,ny in (x+1,y+1),(x+1,y-1),(x-1,y-1),(x-1,y+1):
            sm += self.dic[(nx,ny)]
        return sm


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)




re =Solution()
print(re)