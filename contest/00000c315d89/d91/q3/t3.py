from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        g =[[] for _ in range(n)]
        ind = [0]*n
        for a,b in edges:
            ind[a] +=1
            ind[b] +=1
            g[a].append(b)
            g[b].append(a)
        visited ={}
        cand =deque([(0,1)])
        while cand:
            p,lev = cand.popleft()
            visited[p]=lev
            for a in g[p]:
                if a not in visited:
                    cand.append((a,lev+1))
        blev = visited[bob]
        #print(blev,bob)
        cur = bob
        for _ in range(blev//2):
            amount[cur] = 0 
            k = visited[cur]
            for a in g[cur]:
                if visited[a]<k:
                    cur = a
        if blev %2 ==1 :
            amount[cur] = amount[cur] //2
        #print(cur,amount,blev)
        cand = set()
        for i in range(1,n):
            if ind[i] ==1:
                cand.add(i)
        mx = -10**10
        def dfs(x,cur):
            nonlocal mx
            k = visited[x]
            cur = cur + amount[x]
            if x in cand:
                mx  =max(mx,cur)
            for a in g[x]:
                if visited[a]> k:
                    dfs(a,cur)
        dfs(0,0)
        return mx
    
                
            
            
        
        




re =Solution().mostProfitablePath(edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6])
print(re)