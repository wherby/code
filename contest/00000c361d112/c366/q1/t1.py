from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        a1,a2 = 0,0
        for i in range(1,n+1):
            if i %m ==0:
                a2+=i
            else:
                a1 +=i 
        return a1-a2




re =Solution()
print(re)