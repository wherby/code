from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution(object):
    def minimumTotalPrice(self, n, edges, price, trips):
        """
        :type n: int
        :type edges: List[List[int]]
        :type price: List[int]
        :type trips: List[List[int]]
        :rtype: int
        """
        g= [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        ind =[0]*n
        levelDic={}
        pl = [-1]*n
        def dfs(a,p,level):
            pl[a] =p
            levelDic[a] =level
            for b in g[a]:
                if b ==p:continue
                dfs(b,a,level+1)
        dfs(0,-1,0)
        for a,b in trips:
            if a ==b :
                ind[a] +=1
            else:
                if levelDic[a] > levelDic[b]:
                    a,b = b,a 
                while levelDic[b]> levelDic[a]:
                    ind[b] +=1
                    b = pl[b]
                while a != b:
                    ind[a] +=1
                    ind[b] +=1
                    a = pl[a]
                    b = pl[b]
                ind[a] +=1
        pp = [0]*n
        for i in range(n):
            pp[i] = ind[i] *price[i]
        @cache
        def dfs(a,hf,p):
            ret = 0 
            if hf:
                ret += pp[a] //2
                for b in g[a]:
                    if b ==p:continue
                    ret += dfs(b,0,a)
                return ret
            else:
                ret += pp[a]
                for b in g[a]:
                    if b == p: continue
                    ret += min(dfs(b,0,a), dfs(b,1,a))
                return ret
        return min(dfs(0,0,-1),dfs(0,1,-1))




re =Solution().minimumTotalPrice(n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]])
print(re)