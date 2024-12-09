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
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        dp = [10**20]*k
        dp[-1] = 0
        acc = 0
        ret = -10**20
        for i,a in enumerate(nums):
            acc +=a 
            ret = max(ret,acc-dp[i%k])
            dp[i%k] = min(acc,dp[i%k])
        return ret





re =Solution().maxSubarraySum(nums = [-1,-2,-3,-4,-5], k = 4)
print(re)