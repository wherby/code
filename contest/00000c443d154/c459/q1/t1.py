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
    def checkDivisibility(self, n: int) -> bool:
        ls = [int(a) for a in str(n)]
        x,y = 0,1 
        for a in ls :
            x +=a
            y *=a 
        return n %(x+y) ==0 





re =Solution()
print(re)