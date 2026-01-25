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
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = n-1
        for i in range(n-2,-1,-1):
            if nums[i] >= nums[i+1]:
                return cnt
            else:
                cnt-=1
        return cnt




re =Solution().minimumPrefixLength([1,2,3,4,5])
print(re)