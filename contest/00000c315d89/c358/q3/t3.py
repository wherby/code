from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        sl = SortedList([])
        mx = abs(nums[-1] -nums[0])
        for i,a in enumerate(nums):
            if i>= x:
                sl.add(nums[i-x])
            if sl:
                k = sl.bisect_right(a)
                if k >0:
                    mx = min(mx,abs(a- sl[k-1]))
                if k < len(sl):
                    mx = min(mx,abs(a-sl[k]))
                mx = min(mx,abs(a -sl[-1]))
            
        return mx





re =Solution()
print(re)