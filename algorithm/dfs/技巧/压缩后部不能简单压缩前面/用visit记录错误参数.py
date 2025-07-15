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
        cnt = 0
        visit = {}
        while st:
            cnt +=1
            if cnt >10:
                break
            tmp = []
            #print(len(st),st)
            for state,a,b,cnt in st:
                for c in g[a]:
                    for d in g[b]:
                        if label[c] == label[d] and (((1<<c) & state)== 0) and (((1<<d)&state) == 0) and c !=d:
                            ns =state | (1<<c) | (1<<d)
                            np = label[c]
                            #print(c,d,bin(state), (1<<c)&state )
                            if (ns,np) not in visit:
                                visit[(ns,np)] =1 
                                tmp.append((state | (1<<c) | (1<<d),c,d,cnt+2))
                                mx = max(mx,cnt+2)
            st = tmp
        return mx
        
        







re =Solution().maxLen( n = 4, edges = [[0,2],[0,3],[3,1]], label = "bbac")
print(re)