from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        vist={}
        st= []
        for i,a in enumerate(nums):
            heapq.heappush(st,(a,i))
        sm = sum(nums)
        ret = []
        for idx,c in queries:
            if idx not in vist:
                vist[idx] = 1 
                sm -= nums[idx]
            while st and c :
                b,i = heapq.heappop(st)
                if i not in vist:
                    vist[i] =1
                    sm -=b
                    c -=1
            ret.append(sm)
        return ret
            





re =Solution().unmarkedSumArray(nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]])
print(re)