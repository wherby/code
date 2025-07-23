# https://leetcode.cn/problems/network-recovery-pathways/solutions/3728371/er-fen-da-an-dag-dppythonjavacgo-by-endl-anax/
from typing import List, Tuple, Optional

from collections import defaultdict,deque

from heapq import heappop,heappush 

import math
INF  = math.inf

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        g = defaultdict(list)
        n = len(online)
        mx = 0
        for a,b,c in edges:
            if online[a] and online[b]:
                g[a].append((b,c))
                mx = max(mx,c)
        l,r = -1, mx+1
        def verify(md):
            st = [(0,0)]
            visit ={}
            while st:
                cost,a = heappop(st)
                if a in visit:
                    continue
                if cost > k:
                    return False
                if a == n-1:
                    return True
                visit[a] = 1
                for b,c in g[a]:
                    if c >=md:
                        heappush(st,(cost+c,b))
            return False
        while l <r :
            md = (l+r+1)>>1
            #print(verify(md),md,g)
            if verify(md):
                l = md 
            else:
                r = md -1
        return l if l <=mx and l >=0 else -1



#re =Solution().findMaxPathScore( edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], online = [True,True,True,False,True], k = 12)
re =Solution().findMaxPathScore( edges = [], online = [True,True,True,False,True], k = 12)
edges = [[4,8,51],[6,7,46],[7,9,72],[7,8,14],[8,10,59],[2,5,25],[9,10,55],[3,4,30],[4,5,10],[3,10,28],[4,6,36],[1,7,58],[1,6,95],[2,6,14],[1,9,48],[6,10,64],[8,9,36],[7,10,65],[1,5,95],[5,10,36],[5,8,6],[0,7,59],[5,6,52],[0,9,11],[4,9,87],[3,8,44],[3,6,19],[4,7,63],[0,2,89],[2,4,94],[3,9,80],[5,7,85],[5,9,13],[6,8,17],[0,1,97],[0,8,89],[0,3,95],[0,6,56],[2,8,96],[2,3,41],[4,10,17],[1,3,91],[3,5,74],[1,4,61],[2,10,88],[0,4,45],[2,9,70],[3,7,37],[1,2,52],[0,5,80],[2,7,31],[1,8,69],[1,10,60]]
online =[True,True,False,True,True,True,False,True,True,True,True]
k = 250
#re =Solution().findMaxPathScore( edges , online , k )
print(re)