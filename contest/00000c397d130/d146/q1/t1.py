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
    def countSubarrays(self, nums: List[int]) -> int:
        cnt =0
        n = len(nums)
        for i in range(2,n):
            if  (nums[i] + nums[i-2])*2 == nums[i-1]:
                cnt +=1
        return cnt





re =Solution()
print(re)