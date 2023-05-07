from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ret = []
        sl = SortedList()
        for i in range(k):
            sl.add(nums[i])
        ret.append(sl[x-1]  if sl[x-1]< 0 else 0)
        for i in range(n-k):
            sl.remove(nums[i])
            sl.add(nums[i+k])
            ret.append(sl[x-1] if sl[x-1]< 0 else 0)
        return ret



re =Solution().getSubarrayBeauty(nums = [5], k = 1, x = 1)
print(re)