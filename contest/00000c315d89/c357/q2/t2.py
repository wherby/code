from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        isGood= False
        pls = [0]
        for a in nums:
            pls.append(pls[-1]+a) 
        @cache
        def dfs(l,r):
            nonlocal isGood
            if l>=r-1:
                isGood = True
                return 
            if pls[r]- pls[l]>=m:
                dfs(l,r-1)
            if pls[r+1]-pls[l+1]>=m:
                dfs(l+1,r)
            if pls[r+1] -pls[2]>=m and pls[2]>=m:
                dfs(l+2,r)
            if pls[r-1]-pls[l]>=m and pls[r+1]-pls[r-1] >=m:
                dfs(l,r-2)
            return
        n =len(nums)
        dfs(0,n-1)
        return isGood




re =Solution().canSplitArray(nums = [1], m = 5 )
print(re)