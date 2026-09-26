# https://leetcode.cn/problems/maximum-score-of-non-overlapping-intervals/description/?envType=daily-question&envId=2026-09-12
from typing import List, Tuple, Optional
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        pt = set()
        pt.add(0)
        for a,b,_ in intervals:
            pt.add(a)
            pt.add(b)
        pts = list(pt)
        pts.sort()
        dic = {}
        n = len(pts)
        for i,a in enumerate(pts):
            dic[a] = i 
        dp = [[0]*(n) for _ in range(5)]
        dpr = [[()]*n for _ in range(5)]
        rd = [[] for _ in range(n)]
        for i,(a,b,c) in enumerate(intervals):
            rd[dic[b]].append((a,b,c,i))
        #print(pts,n)
        mx = 0
        res = []
        for i in range(1,n):
            for j in range(4,0,-1):
                dp[j][i] = dp[j][i-1]
                dpr[j][i] = dpr[j][i-1]
                for a,b,c,idx in rd[i]:
                    sa = dic[a] -1 
                    if dp[j-1][sa]+c > dp[j][i]:
                        ret = list(dpr[j-1][sa])
                        ret.append(idx)
                        ret.sort()
                        dpr[j][i] = tuple(ret)
                        dp[j][i] = dp[j-1][sa]+c
                    elif dp[j-1][sa]+c == dp[j][i] :
                        ret = list(dpr[j-1][sa])
                        ret.append(idx)
                        ret.sort()
                        if tuple(ret) < dpr[j][i]:
                            dpr[j][i] = tuple(ret)
       # print(dp,dpr)
        return list(dpr[4][n-1])
    
re = Solution().maximumWeight(intervals = [[1,1,1000000000],[1,1,1000000000],[1,1,1000000000],[1,1,1000000000]])
print(re)