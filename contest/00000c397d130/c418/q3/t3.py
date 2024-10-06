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
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ind = [[0] for _ in range(n)]
        for a,b in edges:
            ind[a] +=1
            ind[b] +=1
        x,y =1,n 
        for a in range(int(math.sqrt(n)),0,-1):
            if n%a ==0:
                x,y = a,n//a 
                break
        ret = [[-1]*x for _ in range(n)]
        





re =Solution()
print(re)