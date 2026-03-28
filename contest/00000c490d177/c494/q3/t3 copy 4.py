from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf




class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        max_val = 0
        for a in nums:
            max_val |= a
        size = (1 << (max_val.bit_length() + 1)) if max_val > 0 else 1
        
        dp = [-1] * size
        dp[0] = 0 
        
        for a in nums:
            ndp = dp[:] 
            for i in range(size):
                if dp[i] >= 0:
                    nxt = i ^ a
                    if nxt < size:  
                        ndp[nxt] = max(ndp[nxt], dp[i] + 1)
            dp = ndp
        
        if target < size and dp[target] >= 0:
            return len(nums) - dp[target]
        return -1
        





re =Solution().minRemovals([2,6],6)
print(re)