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

from itertools import pairwise
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n= len(nums)
        dp =[[-n-2]*n for _ in range(3)]
        dp[0][0] = 0
        if nums[1]<= nums[0]:
            return False
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                dp[0][i] = dp[0][i-1]+1
                dp[2][i] = max(dp[2][i-1] + 1,dp[1][i-1]+1)
            if nums[i]< nums[i-1]:
                dp[1][i] = max(dp[1][i-1] +1,dp[0][i-1] +1)
            #print(dp)
        return dp[2][-1]>0





re =Solution().isTrionic([8,9,4,6,1])
print(re)