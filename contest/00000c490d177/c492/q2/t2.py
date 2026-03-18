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
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        sm =sm1 =sum(nums)
        ret = -1 
        prd =1 
        sm -= nums[-1]
        for i in range(n-1,0,-1):
            if sm==prd:
                ret = i 
            if prd >sm1:
                break
            sm-=nums[i-1]
            prd*=nums[i]
        return ret




re =Solution()
print(re)