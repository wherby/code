# https://leetcode.cn/problems/elevator-requests-ii/submissions/742488147/ 
# 这里虽然还是 N**2 的复杂度，还是会出现OOM ，

from functools import cache
class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        allP = sorted(set([start] + requests))
        N = len(allP)
        
        startIdx = allP.index(start)
        
        @cache
        def dp(i,j,p):
            if i ==0 and j ==N-1:
                return 0 
            ret =10**30
            rem = N-(j-i+1)
            if i >0:
                dis = allP[p] -allP[i-1]
                ret = min(ret,dp(i-1,j,i-1)+dis*rem)
            if j < N-1:
                dis= allP[j+1] -allP[p]
                ret = min(ret,dp(i,j+1,j+1)+dis*rem)
            return ret 
        return dp(startIdx,startIdx,startIdx)