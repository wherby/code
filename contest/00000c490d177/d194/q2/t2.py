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
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        cnt = 0
        acc =0
        for i,a in enumerate(nums):
            if minK<=a and a <= maxK:
                acc +=1
                cnt +=acc 
            else:
                acc =0
        return cnt





re =Solution()
print(re)