## DFS (i,j) 不能在循環裏再循環k
# https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/
# contest\00000c361d112\c393\q4\t4.py  裏面有k 會timeout
# contest\00000c361d112\c393\q4\t4 copy.py
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n = len(nums)
        m = len(andValues)
        @cache
        def dfs(i,j,acc):
            ret = 10**10
            if i ==n and j ==m and acc == -1:
                return 0
            if j ==m or i==n :
                return 10**10
            acc =acc&nums[i]
            ret=min(ret,  dfs(i+1,j,acc))
            if acc ==andValues[j]:
                ret = min(ret,dfs(i+1,j+1,-1) + nums[i])
            
            return ret
        ret =dfs(0,0,-1)
        return ret if ret< 10**10 else -1
            

re = Solution().minimumValueSum( nums = [1,4,3,3,2], andValues = [0,3,3,2])
print(re)


