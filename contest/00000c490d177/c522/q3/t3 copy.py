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
    def maxAlternatingSum(self, nums: list[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        
        INF = float('inf')
        

        dp0_1 = nums[0]
        dp1_1 = -INF
        f0_1 = -INF
        f1_1 = -INF

        dp0_2 = -INF
        dp1_2 = -INF
        
        ans = dp0_1
        
        for i in range(1, n):
            x = nums[i]
 
            dp0 = max(x, dp1_1 + x)
            dp1 = dp0_1 - x
    
            f0 = -INF
            if f1_1 != -INF:
                f0 = max(f0, f1_1 + x)         
            if dp1_2 != -INF:
                f0 = max(f0, dp1_2 + x)        #
                
            f1 = -INF
            if f0_1 != -INF:
                f1 = max(f1, f0_1 - x)       
            if dp0_2 != -INF:
                f1 = max(f1, dp0_2 - x)       

            ans = max(ans, dp0, dp1, f0, f1)
            

            dp0_2, dp1_2 = dp0_1, dp1_1
            dp0_1, dp1_1 = dp0, dp1
            f0_1, f1_1 = f0, f1
            
        return ans




re =Solution().maxAlternatingSum([10,-5,-100])
print(re)