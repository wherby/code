from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
from collections import Counter



class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        dp =[0]*(r+1)
        dp[0] = 1
        c = Counter(nums)
        mod = 10**9+7
        for k,v in c.items():
            dp2 = [0]*(r+1)
            if k ==0:
                for i in range(r+1):
                    dp2[i] = dp[i]*(v)
            else:
                for i in range(v,0,-1):
                    t = k*i
                    for j in range(r-t+1):
                        dp2[j+t]+=dp[j]
                    #print(dp,dp2)
            for i in range(r+1):
                dp[i] += dp2[i]
                dp[i] %=mod
            #print(dp,dp2)
        return sum(dp[l:r+1])%mod




re =Solution().countSubMultisets(nums = [1,2,1,3,5,2], l = 3, r = 5)
print(re)