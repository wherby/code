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
    def minOperations(self, nums: List[int]) -> int:
        zidx = -1
        for i,a in enumerate(nums):
            if a == 0:
                zidx = i 
                break
        n = len(nums)
        isFLip = False
        if nums[(zidx+1)%n] != 1:
            nums = nums[::-1]
            zidx= n-1-zidx 
            isFLip = True
        nlst= nums[zidx:] + nums[:zidx]
        for i,a in enumerate(nlst):
            if a != i :
                return -1 
        return min(zidx+isFLip, n-zidx+2 -isFLip)





re =Solution()
print(re)