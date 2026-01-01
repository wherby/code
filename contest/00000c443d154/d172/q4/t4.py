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
    def lastInteger(self, n: int) -> int:
        
        left = n 
        ret = 1 
        step = 1 
        op = True 

        while left>1:
            if not op and  left %2 ==0 :
                ret += step
            left -= left //2 
            step *=2 
            op = not op 
        return ret




re =Solution().lastInteger(3)
print(re)