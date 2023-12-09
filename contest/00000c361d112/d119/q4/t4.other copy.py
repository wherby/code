from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf


class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        d=[[10**10]*n for i in range(n)]
        ans=0
        for mask in range(2**n):
            s=set()
            for i in range(n):
                if (mask>>i)&1:
                    s.add(i)
            dct=defaultdict(dict)        
            for a,b,v in roads:
                if a in s and b in s:
                    if b not in dct[a]:
                        dct[a][b]=v
                        dct[b][a]=v
                    else:
                        dct[a][b]=min(dct[a][b],v)
                        dct[b][a]=min(dct[b][a],v)
            check=True
            for i in s:
                ss=set()
                h=[[0,i]]
                while h:
                    di,v=heappop(h)
                    ss.add(v)
                    for y in dct[v]:
                        if di+dct[v][y]<=maxDistance and y not in ss:
                            heappush(h,[di+dct[v][y],y])
                if ss!=s:
                    check=False
                    break
            if check:
                ans+=1
        return ans



re =Solution().numberOfSets(10,430,[[3,2,237],[3,1,79],[6,1,84],[6,1,103],[9,6,453],[3,1,342],[3,1,201],[8,0,439],[7,5,467],[4,3,99],[8,7,146],[8,7,335],[6,1,512],[1,0,498],[5,3,241],[5,2,202],[4,1,443],[2,0,69],[2,1,450],[6,3,352],[2,0,438],[4,0,95],[6,1,257],[5,1,271],[8,1,80],[9,1,452],[3,1,57],[9,7,361],[8,4,105]])
print(re)