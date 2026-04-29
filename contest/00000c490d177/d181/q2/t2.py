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
    def compareBitonicSums(self, nums: list[int]) -> int:
        mx = max(nums)
        idx = nums.find(mx)
        a = sum(nums[:idx+1])
        b = sum(nums[idx:])
        if a <b


re =Solution()
print(re)