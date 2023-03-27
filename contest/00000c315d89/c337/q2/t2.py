from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        ls = [0]*(n*n)
        if grid[0][0]!=0:
            return False
        for i in range(n):
            for j in range(n):
                ls[grid[i][j]] = [i,j]
        #print(ls)
        for  i in range(1,n*n):
            px,py = ls[i-1]
            x,y = ls[i]
            if abs(x-px)*abs(y-py)!=2:
                return False
        return True




re =Solution().checkValidGrid([[24,11,22,17,4],[21,16,5,12,9],[6,23,10,3,18],[15,20,1,8,13],[0,7,14,19,2]])
print(re)