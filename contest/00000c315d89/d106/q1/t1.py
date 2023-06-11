from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def isFascinating(self, n: int) -> bool:
        nst = str(n) + str(2*n) +str(3*n)
        for i in range(1,10):
            if str(i) not in nst:
                return False
        return len(nst) ==9
        return True





re =Solution()
print(re)