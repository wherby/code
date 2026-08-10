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
    def maxPairStrength(self, nums: list[int]) -> int:
        n = len(nums)
        mx = 0 
        for i in range(n):
            for j in range(i):
                mx = max(mx, nums[i]*nums[j] /math.gcd(nums[i],nums[j]))
        return mx





re =Solution()
print(re)