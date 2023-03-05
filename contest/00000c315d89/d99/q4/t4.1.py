from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        g = [[] for _ in range(len(edges)+1)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        sg = {(x,y) for x,y in guesses}
        
        def dfs(x,p):
            res = 0
            res += (p,x) in sg
            for a in g[x]:
                if a != p :
                    res += dfs(a,x)
            return res
        cnt0 = dfs(0,-1)
        #print(cnt0)
        ans = 0
        def reRoot(x,y,cnt):
            nonlocal ans
            if cnt >=k:
                ans +=1
            for a in g[x]:
                if a != y:
                    reRoot(a,x,cnt - ((x,a) in sg ) +((a,x) in sg))
        reRoot(0,-1,cnt0)
        return ans
        
        
re =Solution().rootCount(edges = [[0,1],[1,2],[2,3],[3,4]], guesses = [[1,0],[3,4],[2,1],[3,2]], k = 1)
print(re)