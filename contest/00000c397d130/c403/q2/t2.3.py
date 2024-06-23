# https://leetcode.cn/problems/find-the-minimum-area-to-cover-all-ones-i/solutions/2819335/bian-li-pythonjavacgo-by-endlesscheng-6po1/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    
    def minimumArea(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ls1= [sum(a) for a in grid]
        ls2 = [sum(a) for a in zip(*grid)]
        a,b = m,n
        for i in range(m):
            if ls1[i]==0:
                a-=1
            else:
                break
        for i in range(a):
            if ls1[m-1-i]==0:
                a-=1
            else:
                break
        for i in range(n):
            if ls2[i]==0:
                b-=1
            else:
                break
        for i in range(b):
            if ls2[n-1-i]==0:
                b-=1
            else:
                break
        return a*b


re =Solution().minimumArea([[0,1,1,1]])
print(re)