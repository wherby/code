from typing import List, Tuple, Optional

import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9+7 
        g = [[] for _ in range(n)]
        for a,b,c in roads:
            g[a].append((b,c))
            g[b].append((a,c))
        visit=[0]*n 
        mx = [10**10]*n
        st = [(0,0,0)]
        visit[0] = 1 
        

        while st:
            nod,cst,fr = heapq.heappop(st)
            cst = cst %mod
            if cst < mx[nod]:
                mx[nod] = cst
                visit[nod] = visit[fr]
            elif cst == mx[nod]:
                visit[nod] += visit[fr]
                continue
            else:
                continue
            for b,c in g[nod]:
                if b == fr: continue
                if c + cst <= mx[b]:
                    heapq.heappush(st,(b,c +cst, nod))
        #print(visit,mx)
        return visit[-1] %mod

re = Solution().countPaths(n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]])
print(re)

            