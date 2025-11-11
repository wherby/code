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
    def minimumDistance(self, nums: List[int]) -> int:
        re = 10**10
        ls  = defaultdict(list)
        for i,a in enumerate(nums):
            ls[a].append(i)
        for k,v in ls.items():
            if len(v)>=3:
                m = len(v) 
                for i in range(m-2):
                    re = min(re, 2*(v[i+2] -v[i]))
        return re if re < 10**10 else -1





re =Solution()
print(re)