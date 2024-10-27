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
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i,p in enumerate(parent):
            if p == -1:continue
            g[p].append(i)
        
        dic =defaultdict(list)
        ##print(g)
        def dfs(i):
            #print(i,s[i],dic[s[i]],dic,parent[i])
            if s[i] in dic and len(dic[s[i]]) >0:
                #print(parent[i],dic[s[i]][-1],s[i])
                parent[i] = dic[s[i]][-1]
            dic[s[i]].append(i)
            for b in g[i]:
                dfs(b)
            dic[s[i]].pop()
        
        dfs(0)
        #print(parent)
        g = [[] for _ in range(n)]
        for i,p in enumerate(parent):
            if p == -1:continue
            g[p].append(i)
        res = [0]*n

        def dfs(i):
            ret = 1 
            for a in g[i]:
                ret += dfs(a)
            res[i] = ret 
            return ret
        dfs(0)
        return res
            
        




re =Solution().findSubtreeSizes(parent = [-1,10,0,12,10,18,11,12,2,3,2,2,2,0,4,11,4,2,0], s = "babadabbdabcbaceeda")
print(re)