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
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        mx = energy[-1]
        for i in range(k):
            ls =[]
            for j in range(i,n,k):
                ls.append(energy[j])
            acc=0
            for a in ls:
                if acc<0:
                    acc =0
                acc+= a 
            mx = max(mx,acc)
        return mx




re =Solution()
print(re)