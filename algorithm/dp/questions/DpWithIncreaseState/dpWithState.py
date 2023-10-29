# https://leetcode.cn/contest/weekly-contest-369/problems/minimum-increment-operations-to-make-array-beautiful/
# https://leetcode.cn/circle/discuss/ItEVoI/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        
        @cache 
        def dfs(i,j):
            if i <0:
                return 0 
            res = max(k-nums[i],0) + dfs(i-1,0)
            if j <2:
                res = min(res,dfs(i-1,j+1))
            return res
        return dfs(len(nums)-1,0)