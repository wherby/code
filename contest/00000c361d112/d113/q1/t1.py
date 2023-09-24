from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        def verify(ls):
            for i in range(1,n):
                if nums[i]<nums[i-1]:
                    return False
            return True
        for i in range(n):
            if verify(nums):
                return i 
            nums = [nums[-1]]+ nums[:-1]
        return -1





re =Solution()
print(re)