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
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        n = len(tasks)
        pls = [0]
        for a in tasks:
            pls.append(pls[-1] + a )
        ret = []
        cur = 0
        for s in shifts:
            cur +=s 
            t= bisect_right(pls,cur)
            if t>n:
                ret.append(0)
                cur = 0 
            else:
                ret.append(n+1-t)
        return ret





re =Solution().countTasks(tasks = [1,4,4], shifts = [9,1,4])
print(re)