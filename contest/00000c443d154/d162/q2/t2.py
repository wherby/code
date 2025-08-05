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
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l,r = 1,n

        def verify(mid):
            for i in range(mid-1,n):
                if nums[i-mid+1]*k >= nums[i]:
                    return True
            return False

        while l<r:
            mid =(l+r+1)>>1
            if verify(mid):
                l=mid
            else:
                r = mid-1
        return n-l
        



nums = [1]*100000 + [2]*10000 + [10000]*199999
re =Solution().minRemoval(nums = [4,6], k = 2)
print(re)