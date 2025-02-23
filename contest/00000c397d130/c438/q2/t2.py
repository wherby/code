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
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        st =[]
        for i,a in enumerate(grid):
            a.sort(reverse= True)
            st.extend(a[:limits[i]])
        st.sort(reverse= True)
        return sum(st[:k])





re =Solution()
print(re)