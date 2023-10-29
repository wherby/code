from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1]*(target +1)
        dp[0] =0
        for a in nums:
            if a > target:continue
            for j in range(target,a-1,-1):
                #print(j,a)
                if dp[j-a] >=0:
                    #print(j-a,a)
                    dp[j] = max(dp[j], dp[j-a]+1)
            #print(a,dp)
        return dp[target]
        




re =Solution().lengthOfLongestSubsequence([3,5,2,3,4],12)
print(re)