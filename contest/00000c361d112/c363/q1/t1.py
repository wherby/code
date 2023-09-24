from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum([a for i,a in enumerate( nums) if bin(i).count('1') ==k])





re =Solution().sumIndicesWithKSetBits(nums = [5,10,1,5,2], k = 1)
print(re)