from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        def getG(pair,rate):
            g = defaultdict(list)
            for (a,b),r in zip(pair,rate):
                g[a].append((b,r))
                g[b].append((a,1/r))
            return g 
        
        def dfs(g, st,amount):
            ret = defaultdict(int)
            cand=[(st,amount)]
            while cand:
                tmp =[]
                for a,c1 in cand:
                    if ret[a] >=c1:continue
                    ret[a] = c1
                    for b,c2 in g[a]:
                        if c1*c2 > ret[b]:
                            tmp.append((b,c1*c2))
                cand = tmp
            return ret

        g1 = getG(pairs1,rates1)
        ret1 = dfs(g1,initialCurrency,1)
        g2 = getG(pairs2,rates2)

        mx = 0 
        for k,v in ret1.items():
            ret2 = dfs(g2,k,v)
            mx =max(mx,ret2[initialCurrency])
        return mx


        





re =Solution().maxAmount(initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0,3.0], pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], rates2 = [4.0,5.0,6.0])
print(re)