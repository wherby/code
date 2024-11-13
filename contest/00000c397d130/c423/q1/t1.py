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
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dp=[0]*n 
        st = 0
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                st +=1
            else:
                st = 0
            dp[i] = st
        for i in range(n):
            if dp[i]>=k-1 and i+k < n and dp[i+k] -dp[i+1] == k-1:
                return True
        return False




re =Solution().hasIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1], k = 3)
print(re)