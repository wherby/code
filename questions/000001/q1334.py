from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g=[[] for _ in range(n)]
        dic ={}
        for a,b,c in edges:
            if c <= distanceThreshold:
                g[a].append(b)
                g[b].append(a)
                dic[(a,b)] =c 
                dic[(b,a)] =c

        def dfs(i, cst):
            if cst > distanceThreshold:
                return 
            if i in visit and cst >visit[i]:
                return
            visit[i] = cst
            for a in g[i]:
                dfs(a,cst+dic[(a,i)])
            return
        mn = n+1
        ret =-1
        
        for i in range(n):
            visit =defaultdict()
            dfs(i,0)
            #print(i,len(visit),visit)
            if  len(visit) <=mn:
                ret = i 
                mn = len(visit)
        return ret  

re =Solution().findTheCity(6, [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]],20)
print(re)