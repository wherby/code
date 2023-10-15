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
        
        c = Counter(nums)
        dp[0] = 1
        dp[0] += c[0] ##背包问题对0特殊处理
        del c[0]
        mod = 10**9+7
        for k,v in c.items():
            dp2 = dp.copy()
            for i in range(k,r+1):
                dp2[i] +=dp2[i-k]
                dp2[i] %= mod 
            #for i in range(r,(v+1)*k-1,-1):
                if i-(v+1)*k>=0:  ## 另一种写法，及时消去(v+1)个 K 对dp2的影响。这个影响被dp原数组能记录
                    dp2[i] -= dp[i-(v+1)*k]
                dp2[i]%=mod
                
            #print(dp,dp2)
            dp = dp2
            
        return sum(dp[l:r+1])%mod




re =Solution().countSubMultisets(nums = [1,2,1,3,5,2], l = 3, r = 5)
print(re)