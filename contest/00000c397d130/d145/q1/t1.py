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
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        nums.sort()
        if k > nums[0]:
            return -1
        return len(nums)-int(nums[0] ==k)






re =Solution()
print(re)