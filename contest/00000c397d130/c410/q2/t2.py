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
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        dic = defaultdict(list)
        sm =0
        for a,b in edges:
            dic[a].append(b)
            dic[b].append(a)
        
        def dfs(x,p):
            nonlocal sm
            cd =[]
            acc =1
            for b in dic[x]:
                if b == p:continue
                t1 =dfs(b,x)
                acc +=t1
                cd.append(t1)
            
            if len(set(cd)) ==1 or len(cd) ==0:
                #print(x,cd)
                sm +=1
            return acc
        dfs(0,-1)
        return sm
                





re =Solution().countGoodNodes([[6,0],[1,0],[5,1],[2,5],[3,1],[4,3]])
print(re)

#   6
#