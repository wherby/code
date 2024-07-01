# https://leetcode.cn/problems/find-minimum-diameter-after-merging-two-trees/description/

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


def TreeMaxPath(g):
    n  = len(g)
    ans=0
    visit =[0]*n
    def dfs(x):
        nonlocal ans
        visit[x] = 1
        for y,c in g[x]:
            if visit[y] : continue
            dfs(y)
            ans = max(ans,d[x] + d[y]  + c)
            d[x] = max(d[x], d[y] + c)
        #print(x, d,ans)
    d =[0]*n
    for i in range(n):
        if visit[i] ==0:
            dfs(i)
    return ans

def getCenter2(edges):
    ind = defaultdict(int)
    g= defaultdict(list)
    for a,b in edges:
        ind[a]+=1
        ind[b]+=1
        g[a].append(b)
        g[b].append(a)
    cand = []
    for k in ind.keys():
        if ind[k] ==1:
            cand.append(k)
    n = len(ind.keys())
    if n<=2:
        return cand
    visit={}
    while cand:
        tmp = []
        for a in cand:
            visit[a] =1
            for b in g[a]:
                if b not in visit:
                    ind[b] -=1
                    if ind[b] == 1:
                        tmp.append(b)
        cand = tmp
        if len(visit) >=n-2:
            return cand


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n,m = len(edges1)+1,len(edges2)+1
        N = m+n
        g= [[] for _ in range(m+n)]
        edges2 = [(a+n,b+n) for a,b in edges2]
        
        def getTree(edgs):
            g= [[] for _ in range(N)]
            for a,b in edgs:
                g[a].append(b)
                g[b].append(a)
            return g
        
        def getCenter(edges):
            ind = [0]*(N)
            for a,b in edges:
                ind[a]+=1
                ind[b]+=1
            cand = []
            g = getTree(edges)
            for i in range(N):
                if ind[i] ==1:
                    cand.append(i)
            visit = {}
            k = len(edges)+1
            if k <= 2:
                return cand
            while cand:
                tmp = []
                for a in cand:
                    visit[a] =1
                    for b in g[a]:
                        if b not in visit:
                            ind[b] -=1
                            if ind[b] == 1:
                                tmp.append(b)
                cand = tmp
                if len(visit) >=k-2:
                    return cand
        if N ==2:
            return 1
        if N ==3:
            return 2
        cand1,cand2= getCenter2(edges1),getCenter2(edges2)
        
        def getMX(eds):
            g = [[] for _ in range(N)]
            for a,b in eds:
                g[a].append((b,1))
                g[b].append((a,1))
            return TreeMaxPath(g)
        mx = max(getMX(edges1),getMX(edges2))
        for a in cand1:
            for b in cand2:
                T3 = edges2 + edges1 +[[a,b]]
                g = [[] for _ in range(N)]
                for a,b in T3:
                    g[a].append((b,1))
                    g[b].append((a,1))
                mx = max(mx,TreeMaxPath(g))
        return mx
        
            




re =Solution().minimumDiameterAfterMerge(edges1 = [[0,1],[0,2],[0,3]], edges2 = [])
print(re)