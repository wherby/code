from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n=acc = len(nums)
        l,r = 0,n//2
        while r<n and l<n//2 :
            if nums[l]<nums[r]:
                l+=1
                r+=1
                acc -=2
            else:
                r+=1
        return acc





re =Solution().minLengthAfterRemovals([2,3,4])
print(re)