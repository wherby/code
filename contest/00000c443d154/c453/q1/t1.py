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
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dp = [[a,a] for a in nums]
        cnt = [0]*2
        for i in range(n-1):
            if dp[i][0] == -1:
                cnt[0] +=1
                dp[i+1][0] =dp[i+1][0]*-1
            if dp[i][1] == 1:
                cnt[1] +=1
                dp[i+1][1] = dp[i+1][1]*-1 
        mx = n+1 
        if dp[n-1][0] ==1:
            mx = min(mx,cnt[0])
        if dp[n-1][1] == -1:
            mx = min(mx,cnt[1])
        return mx <=k





re =Solution().canMakeEqual( nums = [1,-1,1,-1,1], k = 3)
print(re)