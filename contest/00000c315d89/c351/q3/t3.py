from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        mod = 10**9+7
        acc =0
        last= -1
        for i,a in enumerate(nums):
            if a ==1:
                if last ==-1:
                    last =i 
                    acc =1
                else:
                    if last == i-1: last =i
                    else: 
                        acc = acc*(i-last)%mod 
                        last =i
                        
        return acc





re =Solution().numberOfGoodSubarraySplits( [0,1,1,0,1,1,1,0,1,1,1,0,1,1,1])
print(re)