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
from collections import Counter
class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        c = Counter(nums1+nums2)
        c1 = Counter(nums1)
        ans = 0
        for k,v in c.items():
            if v%2 ==1:
                return -1
            ans += abs(c1[k]-v//2)
        return ans//2





re =Solution()
print(re)