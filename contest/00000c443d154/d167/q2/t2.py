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
    def longestSubarray(self, nums: List[int]) -> int:
        ret = 2 
        n = len(nums)
        state = 2
        for i in range(2,n):
            if nums[i] == nums[i-1]+nums[i-2]:
                state +=1
            else:
                state = 2 
            ret = max(ret,state)
        return ret




re =Solution()
print(re)