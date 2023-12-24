from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        g=defaultdict(list)
        for a,b,c in zip(original,changed,cost):
            g[a].append((b,c))
        
        @cache
        def trace(a,b):
            st=[(0,a)]
            visit= {}
            while st:
                c,a = heapq.heappop(st)
                if a ==b:
                    return c 
                if a in visit:
                    continue
                visit[a] = 1
                for d,c1 in g[a]:
                    if d in visit:continue
                    heapq.heappush(st,(c+c1,d))
            return -1
        sm = 0
        for a,b in zip(source,target):
            re = trace(a,b)
            if re ==-1:
                return -1
            sm +=re 
        return sm



re =Solution().minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20])
print(re)