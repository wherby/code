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
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])
        dir = 2
        curx = 0  
        nx = 0
        ret = []
        for i in range(m):
            if i%2 ==0:
                for j in range(curx,n,2):
                    ret.append(grid[i][j])
                    nx = j
                if nx == n-2:
                    curx = n-1
                else:
                    curx = n-2 
            else:
                for j in range(curx,-1,-2):
                    ret.append(grid[i][j])
                    nx = j
                if nx == 0:
                    curx = 1
                else:
                    curx = 0 
        return ret     






re =Solution().zigzagTraversal( [[1,2,3],[4,5,6],[7,8,9]])
print(re)