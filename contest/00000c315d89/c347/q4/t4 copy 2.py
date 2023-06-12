from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m,n = len(mat),len(mat[0])
        @cache
        def visit(x,y):
            mx = 1
            for i  in range(m):
                if mat[i][y] > mat[x][y]:
                    mx = max(mx,1+ visit(i,y))
            for j in range(n):
                if mat[x][j] > mat[x][y]:
                    mx = max(mx,1+visit(x,j))
            return mx
        mx = 0 
        ls = []
        for i in range(m):
            for j in range(n):
                ls.append((mat[i][j],i,j))
        ls.sort(reverse= True)
        for _,i,j in ls:
            mx = max(mx,visit(i,j))
        return mx





re =Solution().maxIncreasingCells(mat = [[3,1,6],[-9,5,7]])
print(re)