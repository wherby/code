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
    def numberOfAlternatingGroups(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        rcol = [0]*(n+1)
        for i in range(n):
            rcol[i] = colors[i]
        rcol[n] =colors[0]
        ret = []
        acc =0
        for i in range(n):
            if rcol[i] != rcol[i+1]:
                acc +=1
        print(acc)




re =Solution().numberOfAlternatingGroups(colors = [0,1,1,0,1], queries = [[2,1,0],[1,4]])
print(re)