from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        cnt =0 
        m,n =len(grid),len(grid[0])
        ret =[]
        for i in range(m):
            ls = list(grid[i])
            ls.sort()
            ret.append(ls)
        for j in range(n):
            mx =0
            for i in range(m):
                mx = max(mx,ret[i][j])
            cnt +=mx 
        return cnt





re =Solution()
print(re)