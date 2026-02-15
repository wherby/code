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
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        cur = 0 
        def search(start,end):
            m = end-start
            dp= [[0]*(m+1) for _ in range(2)]
            for i in range(m):
                dp[0][i+1] = max(dp[0][i],dp[1][i])
                dp[1][i+1] = dp[0][i]+nums[start+i]
            return max(dp[0][m],dp[1][m])
        acc =0  
        while cur<n:
            start =end =cur 
            while end <n and colors[start]==colors[end]:
                end +=1
            acc += search(start,end)
            cur =end 
        return acc



re =Solution().rob(nums = [1,4,3,5], colors = [1,1,2,2])
print(re)