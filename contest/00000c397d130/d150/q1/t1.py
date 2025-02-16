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
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sm =0 
        nums = nums + [0]*k*2
        for i,a in enumerate(nums[:n]):
            if a > nums[i-k] and a > nums[i+k]:
                sm +=a 
        return sm




re =Solution()
print(re)