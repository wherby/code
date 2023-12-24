from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        mx = -1
        acc = 0
        n = len(nums)
        for i,a in enumerate(nums):
            if i >=2 and a < acc:
                mx = max(acc + a ,mx)
            acc += a
        return mx





re =Solution()
print(re)