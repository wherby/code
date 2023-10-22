from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        pls,pols = [nums[0]],[nums[-1]]
        for i in range(n):
            pls.append(min(nums[i],pls[-1]))
            pols.append(min(pols[-1],nums[n-1-i]))
        ret = 10**9
        for i in range(n):
            if nums[i]>pls[i] and nums[i] > pols[n-i-1]:
                ret = min(ret,nums[i] + pls[i] + pols[n-1-i])
        return ret if ret != 10**9 else -1





re =Solution().minimumSum([5,4,8,7,10,2])
print(re)