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
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 10**9+7
        n = len(nums)
        mx = max(nums)
        dp = [[0]*(mx+1) for _ in range(mx+1)]
        dp[0][0]=1
        for a in nums:
            tdp = [[0]*(mx+1) for _ in range(mx+1)]
            for i in range(mx+1):
                for j in range(mx+1):
                    tdp[i][j] = dp[i][j]
            for i in range(mx+1):
                for j in range(mx+1):
                    c = math.gcd(i,a)
                    d = math.gcd(j,a)
                    tdp[c][j] += dp[i][j]
                    tdp[i][d] += dp[i][j]
            dp = tdp
        ans = 0
        for i in range(1,mx+1):
            ans += dp[i][i]
        return ans%mod




re =Solution().subsequencePairCount([1,2,3,4])
print(re)