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
    def maxProduct(self, nums: List[int]) -> int:
        nums = [abs(a) for a in nums]
        nums.sort()
        nums[-3] = 10**5
        acc = 1 
        for a in nums[-3:]:
            acc=a*acc 
        return acc





re =Solution().maxProduct([-4,-2,-1,-3])
print(re)