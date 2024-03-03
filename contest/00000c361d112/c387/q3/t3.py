from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        hf = n//2
        ret = 10**10
        res =[0]*3
        res[grid[hf][hf]]+=1
        grid[hf][hf] =3
        for i in range(hf):
            res[grid[i][i]] +=1
            grid[i][i] =3
            res[grid[i][n-1-i]] +=1
            grid[i][n-1-i] =3
            res[grid[hf+1+i][hf]] +=1
            grid[hf+1+i][hf] =3
        res2 =[0]*3
        for i in range(n):
            for j in range(n):
                if grid[i][j] ==3: continue
                res2[grid[i][j]] +=1
        for i in range(3):
            for j in range(3):
                if i !=j:
                    ret = min(ret,n*n -res[i]-res2[j])
        #print(ret)
        return ret



re =Solution().minimumOperationsToWriteY( [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]])
print(re)