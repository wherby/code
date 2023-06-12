from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m,n = len(mat),len(mat[0])  
        ind = [[]] *(m*n)
        
        for i in range(m):
            for j in range(n):
                for i1 in range(m):
                    if mat[i1][j] > mat[i][j]:
                        g[i][j].a
        return mx





re =Solution().maxIncreasingCells(mat = [[3,1,6],[-9,5,7]])
print(re)