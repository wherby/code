from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g= [set([]) for _ in range(n)]
        ind =[0]*n
        for a,b in edges:
            ind[a]+=1
            ind[b] +=1
            g[a].add(b)
            g[b].add(a)
        lefs = deque([])
        for i in range(n):
            if ind[i] ==1:
                lefs.append(i)
        #print(lefs)
        while lefs:
            a =lefs.popleft()
            if coins[a] ==0:
                for b in g[a]:
                    ind[b] -=1
                    if ind[b] ==1:
                        lefs.append(b)
                    g[b].remove(a)
                g[a]=[]
        lefs = deque([])
        for i in range(n):
            if ind[i] ==1 and len(g[i]) !=0:
                lefs.append(i)
        for l in lefs:
            for b in g[l]:
                ind[b] -=1
                g[b].remove(l)
            g[l]= []
        lefs = deque([])
        for i in range(n):
            if ind[i] ==1 and len(g[i]) !=0:
                lefs.append(i)
        for l in lefs:
            for b in g[l]:
                ind[b] -=1
                g[b].remove(l)
            g[l]= []
        acc =0
        for i in range(n):
            acc += len(g[i])
        return acc
                
            




re =Solution().collectTheCoins(coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]])
print(re)