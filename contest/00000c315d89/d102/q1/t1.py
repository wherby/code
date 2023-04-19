from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])
        ret =[]
        for i in range(n):
            mx= 0
            for j in range(m):
                mx = max(mx,len(str(grid[j][i])))
            ret.append(mx)
        return ret





re =Solution().findColumnWidth(grid = [[-15,1,3],[15,7,12],[5,6,-2]])
print(re)