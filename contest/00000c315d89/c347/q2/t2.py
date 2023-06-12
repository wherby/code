from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        def countL1(r,c):
            res =set()
            while r>=0 and c>=0:
                res.add(grid[r][c])
                r -=1
                c -=1
            return len(res)
        def countL2(r,c):
            res =set()
            while r<m and c<n:
                res.add(grid[r][c])
                r +=1
                c +=1
            return len(res)
        ret = [[0]*n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                ret[r][c] = abs(countL1(r-1,c-1) - countL2(r+1,c+1))
        return ret





re =Solution()
print(re)