from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        dic = defaultdict(int)
        dic2 = defaultdict(int)
        for a,b in guesses:
            dic[(a,b)] +=1
            dic[(b,a)] -=1
            dic2[(a,b)] +=1
        vis={}
        values=defaultdict(int)
        #print(dic)
        def dfs(a,p,ret):
            vis[a] =1
            ret += dic[(p,a)]
            values[a] = ret
            for b in g[a]:
                if b not in vis:
                    dfs(b,a,ret)
            #print(a,p,ret)
            #return ret
        dfs(0,-1,0)
        vis= {}
        def dfs2(a,p):
            vis[a] =1 
            ret =0 
            ret += dic2[(p,a)]
            for b in g[a]:
                if b not in vis:
                    ret += dfs2(b,a)
            #print(a,p,ret)
            return ret 
        acc =dfs2(0,-1)
        cnt = 0
        #print(values)
        for c in g.keys():
            if acc - values[c]>=k:
                cnt +=1
        return cnt
            
            




re =Solution().rootCount(edges = [[0,1],[1,2],[2,3],[3,4]], guesses = [[1,0],[3,4],[2,1],[3,2]], k = 1)
print(re)