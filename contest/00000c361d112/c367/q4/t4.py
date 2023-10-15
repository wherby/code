from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        isRevert = False
        if m >n:
            isRevert = True
            grid = list(zip(*grid))
        m,n = len(grid),len(grid[0])
        ret = [[0]*n for _ in range(m)]
        ls = [1]*m
        mod = 12345
        for i in range(m):
            acc= 1
            for j in range(n):
                acc*= grid[i][j] 
                acc%=12345
            ls[i] = acc
        for i in range(m):
            acc = 1
            for i1 in range(m):
                if i != i1:
                    acc*=ls[i1]
            pre,pls =[1],[1]
            for j in range(n):
                pre.append(pre[-1]*grid[i][j] %mod)
                pls.append(pls[-1]*grid[i][n-1-j]% mod)
            for j in range(n):
                ret[i][j] = acc * pre[j]*pls[n-1-j] %mod
        if isRevert == True:
            ret = list(zip(*ret))
            ret = [list(a) for a in ret]
        return ret




re =Solution().constructProductMatrix(grid = [[1,2,3],[2,3,4],[1,2,3],[2,3,4]])
print(re)