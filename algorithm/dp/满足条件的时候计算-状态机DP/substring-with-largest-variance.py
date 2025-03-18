# https://leetcode.cn/problems/substring-with-largest-variance/?envType=daily-question&envId=2025-03-16


class Solution:
    def largestVariance(self, s: str) -> int:
        mx =0
        ls = set([a for a in s])

        def get(a,b):
            dp0,dp1 =0,-10**10
            ret = 0
            for c in s:
                if c == a:
                    dp0 =max(dp0 ,0) +1
                    dp1  +=1
                if c == b:
                    dp1=dp0 =max(dp0 ,0)-1
                ret = max(ret,dp1)
            return ret
        ret = 0
        for a in ls:
            for b in ls:
                if a != b:
                    ret = max(ret,get(a,b))
        return ret