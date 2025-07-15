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

fmax = lambda x, y: x if x > y else y
class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        g = [[] for _ in range(n)]
        st =[]
        mx = 1
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            if label[a] == label[b]:
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
                if a >b:
                    a,b = b,a
                for c in g[a]:
                    if ((1<<c)&state):continue
                    for d in g[b]:
                        if label[c] == label[d] and (((1<<c) & state)== 0) and (((1<<d)&state) == 0) and c !=d:
                            ns =state | (1<<c) | (1<<d)
                            np = sorted([c,d])
                            #print(c,d,bin(state), (1<<c)&state )
                            if (ns,np[0],np[1]) not in visit:
                                visit[(ns,np[0],np[1])] =1 
                                tmp.append((state | (1<<c) | (1<<d),c,d,cnt+2))
                                mx = fmax(mx,cnt+2)
            st = tmp
        return mx

edges = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12],[0,13],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[1,13],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],[2,11],[2,12],[2,13],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[3,10],[3,11],[3,12],[3,13],[4,5],[4,6],[4,7],[4,8],[4,9],[4,10],[4,11],[4,12],[4,13],[5,6],[5,7],[5,8],[5,9],[5,10],[5,11],[5,12],[5,13],[6,7],[6,8],[6,9],[6,10],[6,11],[6,12],[6,13],[7,8],[7,9],[7,10],[7,11],[7,12],[7,13],[8,9],[8,10],[8,11],[8,12],[8,13],[9,10],[9,11],[9,12],[9,13],[10,11],[10,12],[10,13],[11,12],[11,13],[12,13]]
label = "ababababababab"
re = Solution().maxLen(14,edges,label)
print(re)
        
        







re =Solution().maxLen( n = 4, edges = [[0,2],[0,3],[3,1]], label = "bbac")
print(re)