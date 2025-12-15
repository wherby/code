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
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def fn(x):
            xb = bin(x)
            return int(xb[:2]+ bin(x)[2:][::-1],base=0)
        nums.sort(key= lambda x: (fn(x),x))
        return nums




re =Solution().sortByReflection([3,5,6,8])
print(re)