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
    def maxOperations(self, nums: List[int]) -> int:
        n =len(nums)
        cnt = 1
        sm = nums[0]+nums[1]
        for i in range(3,n,2):
            if nums[i] + nums[i-1] == sm:
                cnt +=1
            else:
                return cnt





re =Solution()
print(re)