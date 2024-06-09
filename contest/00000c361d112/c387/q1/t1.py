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
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1,arr2=[nums[0]],[nums[1]]
        idx = 2 
        for i in range(idx,n):
            if arr1[-1]>arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1+arr2





re =Solution()
print(re)