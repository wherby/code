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
    def minChanges(self, n: int, k: int) -> int:
        cnt = 0
        for i in range(32):
            if (n>>i) &1 ==1 and (k>>i)&1 == 0:
                cnt +=1
            if (n>>i) &1 ==0 and (k>>i)&1 == 1:
                return -1
        return cnt




re =Solution()
print(re)