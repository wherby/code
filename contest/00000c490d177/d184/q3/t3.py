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
    def maxTotal(self, nums: List[int], s: str) -> int:
        acc = 0
        last0 = -10**10
        acc1 = 0
        for i,a in enumerate(s):
            if a =="1":
                acc1 += nums[i] 
                if acc1 <acc1-nums[i] + last0:
                    acc += acc1-nums[i] + last0 
                    acc1 =0 
                    last0 = nums[i]
            if a =="0":
                acc += acc1 
                last0 =nums[i]
                acc1 =0
        return acc + acc1





re =Solution().maxTotal(nums = [8,5], s = "10")
print(re)