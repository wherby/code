from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        def verify(mid):
            g = [[] for _ in range(n)]
            for a,b,c in edges:
                if c <0:
                    c = mid
                g[a].append((b,c))
                g[b].append((a,c))
            st = [(0,source)]
            visit = {}
            while st:
                c,d = heapq.heappop(st)
                if d in visit:continue
                if d ==destination:
                    return c
                visit[d] =1 
                #if c > target: continue
                for b,c1 in g[d]:
                    if b not in visit:
                        heapq.heappush(st,(c+c1,b))
        l,r = 0,3*10**9
        while l<r:
            mid = (l+r)>>1
            #print(verify(mid))
            if verify(mid)>=target:
                r = mid 
            else:
                l= mid +1
        if l==0 or r ==3*10**9 :
            return []
        se = []
        rem= target- verify(l)
        for a,b,c in edges:
            if c ==-1:
                c = l 
            se.append((a,b,c))
        return se




re =Solution().modifiedGraphEdges(n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5)
print(re)