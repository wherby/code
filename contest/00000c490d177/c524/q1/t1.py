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
    def minDeletions(self, nums: list[int]) -> int:
        cnt = 0 
        for a,b in pairwise(nums):
            if a ==b:
                cnt +=1
        return cnt





re =Solution()
print(re)