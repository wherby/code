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
from itertools import pairwise
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        ret =[]
        for i in range(m-k+1):
            tmp=[]
            for j in range(n-k+1):
                ls = []

                for i1 in range(k):
                    for j1 in range(k):
                        ls.append(grid[i+i1][j+j1])
                ls = list(set(ls))
                ls.sort()
                t =ls[-1]-ls[0]
                for a,b in pairwise(ls):
                    t = min(t,b-a)
                tmp.append(t)
            ret.append(list(tmp))

        return ret




re =Solution().minAbsDiff(grid = [[3,-1]], k = 1)
print(re)