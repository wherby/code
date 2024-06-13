from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
#from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1]<=nums[2]:
            return "none"
        if nums[1] ==nums[2] == nums[0]:
            return "equilateral"
        if nums[1] ==nums[2] or nums[0] ==nums[1]:
            return "isosceles"
        return "scalene"





re =Solution()
print(re)