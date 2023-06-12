from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        acc =0 
        n = len(nums)
        for i in range(n):
            if nums[i] ==1:
                break
            else:
                acc+=1
        for i in range(n-1,-1,-1):
            if nums[i] == n:
                break
            else:
                acc +=1
        if acc >= n:
            acc -=1
        return acc 





re =Solution()
print(re)