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
        if s[0] == '0':
            f0, f1 = 0, nums[0]
        else:
            f0, f1 = float('-inf'), nums[0]
            
        for i in range(1, len(nums)):
            v = nums[i]
            if s[i] == '0':
                f0, f1 = max(f0, f1), max(f0, f1) + v
            else:
                f0, f1 = f1, max(f0, f1) + v
        return f0 if s[-1] == '0' else max(f0, f1)





re =Solution().maxTotal([100,10,40],"011")
print(re)