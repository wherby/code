from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ind = [0]*n 
        for a,b in edges:
            ind[b] +=1
        ls = [i for i,a in enumerate(ind) if a ==0]
        return ls[0] if len(ls) ==1 else -1




re =Solution()
print(re)