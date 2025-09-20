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
    def countStableSubsequences(self, nums: List[int]) -> int:
        # 0,(1,0),1,(2,0),2,(1,1),3,(2,1)
        dp = [0]*4
        mod = 10**9+7
        for a in nums:
            ndp = [0]*5
            if a %2 ==0:
                ndp[0] =1 + dp[2]+dp[3]
                ndp[1] = dp[0]
            else:
                ndp[2] =1 + dp[0]+dp[1]
                ndp[3] = dp[2]
            dp = [(c+d)%mod for c,d in zip(dp,ndp)]
        return sum(dp) %mod




re =Solution().countStableSubsequences([2,3,4,2])
print(re)