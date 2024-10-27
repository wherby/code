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
        def getDp(nums):
            dp=[[0]*(mx+1) for _ in range(n)]
            for i,a in enumerate(nums):
                for j in range(mx+1):
                    dp[i][j] = dp[i-1][j]
                dp[i][a]+= 1
                for j in range(mx,0,-1):
                    k = math.gcd(j,a)
                    dp[i][k] += dp[i-1][j]
            return dp

        
        dp2 =getDp(nums[::-1])
        print(dp2)
        acc= 0
        dp=[[0]*(mx+1) for _ in range(n)]
        for i,a in enumerate(nums):
            dp[i][a]+= 1
            for j in range(mx,0,-1):
                k = math.gcd(j,a)
                dp[i][k] += dp[i-1][j]
            if i != n-1:
                x1 = dp[i]
                x2 = dp2[n-2-i]
                x3= [a*b for a,b in zip(x1,x2)]
                print(x1,x2,sum(x3))
                acc += sum(x3)
        return acc%mod





re =Solution().subsequencePairCount([1,2,3,4])
print(re)