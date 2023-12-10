from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        n = len(nums)
        ls =[]
        for i,a in enumerate(nums):
            if a == mx:
                ls.append(i)
        m = len(ls)
        sm = 0
        ls = [-1] + ls + [n]
        for i in range(1,m+2-k):
            sm += (ls[i]+1) * (ls[i+k]-ls[i+k-1])
        # for l  in range(k):
        #     for i in range(1,m+2-l):
        #         sm += (ls[i] - ls[i-1] )*(ls[i+l] - ls[i+l-1])
                #print(sm)
        return sm





re =Solution().countSubarrays(nums = [1,3,2,3,3], k = 2)
print(re)