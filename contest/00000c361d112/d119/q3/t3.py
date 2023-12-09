from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        mx = 0 
        l = 0 
        dic = defaultdict(int)
        for i,a in enumerate(nums):
            dic[a] +=1
            while dic[a] > k :
                dic[nums[l]] -=1
                l +=1
            mx = max(mx,i-l+1)
        return mx





re =Solution()
print(re)