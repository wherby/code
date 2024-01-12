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
        dic = defaultdict(list)
        for a,b,c in zip(original,changed,cost):
            g[a].append((b,c))
            # tls = [i for  i in range(len(source)) if source.startswith(a,i) and target.startswith(b,i)]
            # for i in tls:
            #     dic[i].append((a,c))
        
        @cache
        def tra(a):
            st = [(0,a)]
            visit = {}
            ret = {}
            while st:
                c,a = heapq.heappop(st)
                if a in visit:continue
                visit[a] = 1
                ret[a] = c
                for b,c1 in g[a]:
                    if b in visit: continue
                    heapq.heappush(st,(c+c1,b))
            return ret
                    
        for a,b,c in zip(original,changed,cost):
            tls =[i for  i in range(len(source)) if source.startswith(a,i)]
            ret = tra(a)
            for i in tls:
                for b in ret.keys():
                    if target.startswith(b,i):
                        c = ret[b]
                        dic[i].append((a,c))
            
        
        n = len(source)
        #print(dic)
        @cache
        def dfs(i):
            if i == n:
                return 0
            ret = 10**20
            if source[i] == target[i]:
                ret= min(ret, dfs(i+1))
            for a,c in dic[i]:
                ret = min(ret,c + dfs(i+len(a)))
            return ret
        res = dfs(0)
        return res if res<10**20 else -1
            



re =Solution().minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20])
print(re)