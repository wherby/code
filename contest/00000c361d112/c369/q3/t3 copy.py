from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def isGood(idx):
            if 0<=idx<n and nums[idx] >=k:
                return True
            else:
                return False
        @cache
        def dfs(i):
            if i >=n:
                return 0
            mn = 10**20
            if isGood(i-2) or isGood(i-1) or isGood(i) or i <2:
                mn =min(mn, dfs(i+1))
            else:
                if i>=2:
                    a = k - nums[i-2]
                    mn =min(mn, a + dfs(i+1))
                if i >=1:
                    a = k - nums[i-1]
                    nums[i-1] = k
                    mn = min(mn,a + dfs(i+2))
                    nums[i-1] -=a
                a = k - nums[i]

                mn = min(mn,dfs(i+3)+a)

            return mn
                
        return dfs(0)   





re =Solution().minIncrementOperations(nums = [13,34,0,13,9,19],k=82)
#re= Solution().minIncrementOperations([2,3,0,0,2],4)
#re =Solution().minIncrementOperations([6,14,17,4,7],22)
print(re)