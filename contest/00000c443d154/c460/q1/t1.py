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
    def maximumMedianSum(self, nums: List[int]) -> int:
        n = len(nums)//3
        nums.sort()
        acc = 0
        for _ in range(n):
            a = nums.pop()
            b = nums.pop()
            acc +=b 
        return acc





re =Solution()
print(re)