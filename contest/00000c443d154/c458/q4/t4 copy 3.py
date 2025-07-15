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

class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        g = [[] for _ in range(n)]
        st =[]
        mx = 1
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            if label[a] == label[b] :
                st.append(((1<<a) + (1<<b),a,b,2))
        if len(st):
            mx =2
        for i in range(n):
            st.append(( 1<<i,i,i,1))
    
        @cache
        def dfs(state,a,b):
            if a > b:
                a,b = b,a
            ret = 0 
            for c in g[a]:
                if ((1<<c)&state):continue
                for d in g[b]:
                    if label[c] == label[d] and (((1<<c) & state)== 0) and (((1<<d)&state) == 0) and c !=d:
                        ns =state | (1<<c) | (1<<d)
                        if c > d:
                            c,d = d,c
                        ret = max(ret, dfs(ns,c,d)+2)
            return ret
        
        for st,a,b,cnt in st:
            mx = max(dfs(st,a,b)+cnt,mx)


        return mx
        
        







re =Solution().maxLen( n = 4, edges = [[0,2],[0,3],[3,1]], label = "bbac")
print(re)