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
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        nums.sort()
        re =[]
        for i in range(n//2):
            re.append(nums[i] + nums[n-1-i])
        return min(re)/2





re =Solution()
print(re)