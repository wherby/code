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
    def maximumScore(self, nums: List[int], s: str) -> int:
        n = len(nums)
        sl= SortedList([])
        sm = 0 
        for i,a in enumerate(s):
            sl.add(nums[i])
            if a =="1":
                sm += sl[-1]
                sl.pop()
            #   print(sl,sm)
        return sm





re =Solution().maximumScore(nums = [2,1,5,2,3], s = "01010")
print(re)