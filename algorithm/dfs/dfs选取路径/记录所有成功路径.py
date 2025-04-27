# https://leetcode.cn/problems/concatenated-divisibility/solutions/3663246/quan-pai-lie-bao-sou-pythonjavacgo-by-en-l4zv/

from typing import List, Tuple, Optional

from functools import cache

import math
INF  = math.inf

class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans =[]
        ls =[]
        nums.sort()
        @cache
        def dfs(state,res):
            if state == 0 and res ==0:
                ans.append(list(ls))
                return True
            if state ==0:
                return False
            for i in range(n):
                if (1<<i)&state:
                    ls.append(nums[i])
                    m = len(str(nums[i] ))
                    t1  = res * (10**m) + nums[i]
                    t1 = t1%k
                    if dfs(state - (1<<i),t1):
                        return True
                    ls.pop()
            return False
        dfs((1<<n)-1,0)
        return ans[0] if len(ans) >0 else []
                    