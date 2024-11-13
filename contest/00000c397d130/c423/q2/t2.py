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
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp=[0]*n 
        st = 0
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                st +=1
            else:
                st = 0
            dp[i] = st
        rdp =[0]*n
        st = 0
        for i in range(n-2,-1,-1):
            if nums[i] <nums[i+1]:
                st +=1
            else:
                st = 0
            rdp[i] = st
        mx = 0 
        for i in range(n-1):
            mx=max(mx, min(dp[i]+1,rdp[i+1] +1))
        #print(dp,rdp)
        return mx





re =Solution().maxIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1])
print(re)