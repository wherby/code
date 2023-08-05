from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        mx = nums[-1]
        for i in range(n-2,-1,-1):
            a = nums[i]
            if a <=mx:
                mx = a + mx
            else:
                mx = a 
        return mx





re =Solution()
print(re)