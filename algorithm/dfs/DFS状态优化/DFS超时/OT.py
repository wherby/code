# https://leetcode.cn/problems/stone-game-v/submissions/742704101/?envType=daily-question&envId=2026-08-17
from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def stoneGameV(self, sv: List[int]) -> int:
        pre =[0]
        n = len(sv)
        for a in sv:
            pre.append(a+pre[-1])
        @cache
        def dfs(l,r):
            if l ==r:
                return 0 
            ret =0
            for i in range(l,r):
                mn = min(pre[i+1]- pre[l] , pre[r+1]-pre[i+1])
                if pre[i+1]- pre[l] == mn:
                    ret = max(ret , pre[i+1]- pre[l] +dfs(l,i))
                if pre[r+1]-pre[i+1] ==mn:
                    ret = max(ret,pre[r+1] - pre[i+1] + dfs(i+1,r))
            return ret 
        return dfs(0,n-1)
from input import nums
re = Solution().stoneGameV(nums)
print(re)