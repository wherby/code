from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList



class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[1]*2 for _ in range(n)]
        for i in range(1,n):
            if nums1[i] >= nums1[i-1]:
                dp[i][0] = dp[i-1][0]+1
            if nums1[i] >= nums2[i-1]:
                dp[i][0] = max(dp[i][0], dp[i-1][1]+1)
            if nums2[i] >= nums1[i-1]:
                dp[i][1] = dp[i-1][0]+1
            if nums2[i] >= nums2[i-1]:
                dp[i][1] = max(dp[i][1],dp[i-1][1]+1)
        return max([max(ls) for ls in dp])
                
        
        




re =Solution().maxNonDecreasingLength(nums1 = [1,3,2,1], nums2 = [2,2,3,4])
print(re)