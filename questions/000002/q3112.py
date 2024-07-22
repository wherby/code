from typing import List, Tuple, Optional
from heapq import heapify,heappop,heappush 

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        dp=[10**10 for _ in range(n)]
        g = [[] for _ in range(n)]
        for a,b,c in edges:
            g[a].append((b,c))
            g[b].append((a,c))
        cand = [(0,0)]
        visit ={}
        while cand:
            c,a= heappop(cand)
            if a in visit:
                continue
            visit[a] =1
            dp[a] = c 
            for b,c1 in g[a]:
                if c + c1 >= disappear[b] or b in visit: continue
                heappush(cand,(c+c1,b))
        return [a if a != 10**10 else -1 for a in dp ]


re = Solution().minimumTime(n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,3,5])
print(re)