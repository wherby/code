# https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-i/submissions/704495906/?envType=daily-question&envId=2026-03-09
# 如果数据范围大的时候，就需要使用容斥原理处理带限制的Combination: 
# https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-ii/solutions/2758868/dong-tai-gui-hua-cong-ji-yi-hua-sou-suo-37jdi/
from functools import cache

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod =10**9+7 

        @cache
        def dfs(a,b):
            if a <0 or b < 0:
                return 0 
            if a==0 and b ==0:
                return 1 
            res = 0
            for i in range(1,min(limit,a)+1):
                res += dfs(b,a-i)
            return res%mod 
        return (dfs(zero,one) + dfs(one,zero))%mod