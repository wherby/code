from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        
        hmax =1
        vmax =1
        # hBars.append(n+2)
        # vBars.append(m+2)
        n1,m1= len(hBars),len(vBars)
        hcur= 1
        vcur = 1
        for i,a in enumerate(hBars):
            if i ==0 or a != hBars[i-1]+1:
                hcur = 2
            else:
                hcur +=1
            hmax=max(hmax,hcur)
        for i,a in enumerate(vBars):
            if i ==0 or a != vBars[i-1]+1:
                vcur = 2
            else:
                vcur +=1
            vmax = max(vmax,vcur)
        return min(vmax,hmax)**2
        





re =Solution()
print(re)