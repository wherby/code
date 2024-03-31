from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        pre = -1
        cnt = 0
        acc = 0
        for a in nums:
            if a != pre:
                cnt +=1
                pre =a 
            else:
                acc += cnt*(cnt+1)//2
                cnt = 1 
                pre =a
        acc += (cnt+1)*cnt//2
        return acc
        




re =Solution().countAlternatingSubarrays( [0,1,1,1])
print(re)