from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        ret = 0
        b = 0
        mod = 10**9+7
        for i, a in enumerate(nums):
            ret += a*a *(b+a)
            b = b*2+a
            b,ret = b%mod,ret %mod
        return ret




re =Solution().sumOfPower([2,1,4])
print(re)