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
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        pre = [0]
        for a in nums:
            pre.append(pre[-1]+a)
        dp = [0]*(n+1) 
        ans = sum(nums[:l])

        for j in range(1,m+1):
            q= deque()
            ndp = [-10**20]*(n+1)
            for i in range(1,n+1):
                ndp[i] = ndp[i-1]
                target = i -l 
                if target>=0:
                    val = dp[target] - pre[target]
                    while q and (dp[q[-1]] - pre[q[-1]]) <= val:
                        q.pop()
                    q.append(target)
                if q and q[0]< i-r:
                    q.popleft()
                if q:
                    t = q[0]
                    cur = pre[i] + (dp[t] - pre[t])
                    ndp[i] = max(ndp[i],cur)
                    ans = max(ans,ndp[i])
            dp = ndp
            #dp[0]=0
        return ans





re =Solution().maximumSum( nums = [1,0,3,4], m = 2, l = 1, r = 2)
print(re)