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
    def minimumK(self, nums: List[int]) -> int:
        l,r = 1,max(len(nums),max(nums))

        def verify(mid):
            tot = 0 
            for a in nums:
                tot += (a+mid -1)//mid
            return tot <=mid**2
        while l<r:
            mid = (l+r)//2
            if verify(mid):
                r = mid
            else:
                l = mid+1
        return l





re =Solution().minimumK([3,7,5])
print(re)