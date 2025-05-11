# 因为 a,d,acc是有取值范围，所以可以直接dfs
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache

class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        g = [[] for _ in range(n)]
        ind = [0]*n 
        for a,b,c in edges:
            g[a].append((b,c))
            ind[b]+=1
        ret = -1
        @cache
        def dfs(a,d, acc):
            nonlocal ret
            if d >t or acc > t:
                return 
            if d == k and acc <t:
                ret = max(ret,acc)
            for b,c in g[a]:
                dfs(b,d+1,acc+c)
            #visit[a] =1
        for i in range(n):
            dfs(i,0,0)
        return ret  





re =Solution().maxWeight( n = 3, edges = [[0,1,6],[1,2,8]], k = 1, t = 6)
re =Solution().maxWeight(  n = 3, edges = [[0,1,1],[1,2,2]], k = 2, t = 4)
print(re)