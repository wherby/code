from functools import cache
from collections import defaultdict,deque
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dic =defaultdict(list)
        n = len(ring)
        for i,a in enumerate(ring):
            dic[a].append(i)
        m = len(key)
        @cache 
        def dfs(idx,k):
            if idx ==m :
                return 0 
            ret = 10**10
            for b in dic[key[idx]]:
                cst = min(abs(k-b), n-abs(k-b))
                ret = min(ret,dfs(idx+1,b)+ cst)
            return ret
        return dfs(0,0)+m
    
re =Solution().findRotateSteps(ring = "godding", key = "gd")
print(re)
