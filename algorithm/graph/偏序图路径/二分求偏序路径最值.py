# https://leetcode.cn/problems/network-recovery-pathways/description/?envType=daily-question&envId=2026-07-03
from typing import List, Tuple, Optional
from heapq import heapify,heappop,heappush 
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        ls = []
        for a,b,c in edges:
            if online[a] and online[b]:
                ls.append((c,a,b))
        if len(ls) ==0:
            return -1
        ls.sort()
        l,r = 0,ls[-1][0]

        def verify(mid):
            g = [[] for _ in range(n)]
            for c,a,b in ls:
                if c >=mid:
                    g[a].append((b,c))
            dp = [1]*n 
            #print(mid,g)
            st =[(-k,0)]
            while st:
                cur,a = heappop(st)
                if cur < dp[a]:
                    dp[a] = cur
                    for b,c in g[a]:
                        heappush(st,(cur+c,b))
            return dp[-1] <=0
        while l < r:
            mid = (l+r+1)>>1
            if verify(mid):
                l= mid 
            else:
                r = mid -1 
        return l if verify(l) else -1
        