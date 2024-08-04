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
    def canAliceWin(self, nums: List[int]) -> bool:
        return sum(nums) != sum([a for a in nums if a <10])*2





re =Solution()
print(re)