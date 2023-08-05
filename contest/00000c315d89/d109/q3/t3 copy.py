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
        dp = [nums[0]]*2
        k1 =(k+1)%2 
        dp[k] = nums[0]
        dp[k1] = nums[0]-x
        mx = max(dp)
        #print(dp)
        for i in range(1,n):
            a = nums[i]
            k = a %2
            k1 =(k+1)%2 
            dp[k] =max( dp[k]+ a,dp[k1] +a -x)
            mx = max(mx,max(dp))
            #print(dp,i,a)
            
        return mx
        





re =Solution().maxScore([9,58,17,54,91,90,32,6,13,67,24,80,8,56,29,66,85,38,45,13,20,73,16,98,28,56,23,2,47,85,11,97,72,2,28,52,33],90)
print(re)