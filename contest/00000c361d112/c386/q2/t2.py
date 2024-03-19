from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        ls = [(a,b) for a,b in zip(bottomLeft,topRight)]
        ls.sort()
        n = len(ls)
        ret = 0
        for i in range(n):
            (x1,y1),(nx1,ny1) =ls[i] 
            for j in range(i):
                (x2,y2),(nx2,ny2) = ls[j]
                if nx2 >x1:
                    #print(x1,nx1,x2,nx2)
                    dx = min( nx2-x1,nx2-x2,nx1-x1)
                    yls=[(y1,ny1),(y2,ny2)]
                    yls.sort()
                    #print(yls)
                    if yls[1][0] < yls[0][1]:
                        dy=min(yls[0][1]-yls[1][0], yls[0][1]-yls[0][0],yls[1][1]-yls[1][0])
                        ret = max(ret,min(dx,dy)**2)
                        #print(dx,dy,ls[i],ls[j])
        return ret




re =Solution().largestSquareArea([[3,2],[1,1]],[[4,5],[5,4]])
print(re)