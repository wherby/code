from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf
import itertools

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        ret = [-1]*n
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        def dfs(i,p):
            cdv =[cost[i]]
            for a in g[i]:
                if a ==p:continue
                tp =dfs(a,i)
                cdv=cdv +tp
            cdv.sort()   
            #print(cdv)
            if len(cdv) < 3:
                ret[i] = 1 
            elif len(cdv)<=6:
                ca = []
                for cand in itertools.combinations(cdv,3):
                    ca.append(cand[0]*cand[1]*cand[2])
                ca.sort()
                if ca[-1]<=0:
                    ret[i] = 0 
                else:
                    ret[i] = ca[-1]
            else:
                cdv = cdv[:3]+ cdv[-3:]
                ca = []
                for cand in itertools.combinations(cdv,3):
                    ca.append(cand[0]*cand[1]*cand[2])
                ca.sort()
                if ca[-1]<=0:
                    ret[i] = 0 
                else:
                    ret[i] = ca[-1]
            return cdv
        dfs(0,-1)
        return ret 

re =Solution().placedCoins(edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]], cost = [1,4,2,3,5,7,8,-4,2])
print(re)
                
                
        




