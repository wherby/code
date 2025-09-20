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
    def smallestAbsent(self, nums: List[int]) -> int:
        c = sum(nums)//len(nums)+1
        st =set(nums)
        while c  in st or c <=0:
            c +=1
        return c





re =Solution().smallestAbsent([-34])
print(re)