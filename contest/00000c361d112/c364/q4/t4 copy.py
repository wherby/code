from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

def get_prime(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    return res

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n+1)]
        pls = get_prime(n)
        plss = set(pls)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        smm =0
        dic = {}
        sameRegion = []
        def dfs2(a,rt):
            ret = 1
            sameRegion.append(a)
            for b in g[a]:
                if b != rt and b not in plss:
                    ret += dfs2(b,a)
            return ret
        
        def dfs(a,rt):
            nonlocal sameRegion
            cnt = 0
            cd= []
            for b in g[a]:
                if b != rt and b not in plss:
                    if b not in dic:
                        sameRegion =[]
                        dfs2(b,a)
                        
                        for c in sameRegion:
                            dic[c] = len(sameRegion)
                    cd.append(dic[b])
            cnt = sum(cd)
            acc = 0
            chs = cnt
            for c in cd:
                acc+=c
                cnt += c* (chs-acc)
            return cnt
                
            
        for p in pls:
            smm +=dfs(p,-1)
        return smm



re =Solution().countPaths(10,[[10,9],[2,10],[1,10],[3,2],[6,10],[4,3],[8,6],[5,8],[7,6]])
print(re)