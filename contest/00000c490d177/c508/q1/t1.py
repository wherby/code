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
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort()
        sm = 0
        for i in range(k):
            sm += nums[-1]*(max(1,mul))
            mul -=1
            nums.pop()
        return sm





re =Solution()
print(re)