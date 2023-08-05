from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        k = nums[0]%2
        dp = [-10**10]*2
        dp[k] = nums[0]
        mx = 0
        #print(dp)
        for i in range(1,n):
            a = nums[i]
            k = a %2
            k1 =(k+1)%2 
            dp[k] =max( dp[k]+ a,dp[k1] +a -x,0)
            mx = max(mx,max(dp))
            #print(dp,i,a)
            
        return mx
        





re =Solution().maxScore(nums = [2,4,6,8], x = 3)
print(re)