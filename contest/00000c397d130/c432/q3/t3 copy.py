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
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        
        def verify(mid):
            g = [[] for _ in range(n)]
            for a,b,c in edges:
                if c <= mid:
                    g[b].append(a)
            visit={}
            ind =[0]*n 
            
            def dfs(a):
                if a in visit:
                    return 0 
                ret = 1 
                visit[a] = 1 
                for b in g[a]:
                    ret += dfs(b)
                return ret
            ret = dfs(0)
            #print(mid,ret,ret==n )
            return ret ==n

        dic = defaultdict(list)
        for a,b,c in edges:
            dic[c].append((a,b))
        keys = list(dic.keys())
        keys.sort()
        m = len(keys)
        l,r = 0,m-1
        while l <r:
            mid =(l+r)>>1
            if verify(keys[mid]):
                r= mid 
            else:
                l = mid+1
        if verify(keys[l]):
            return keys[l]
        return -1




re =Solution().minMaxWeight(n = 5, edges = [[1,0,1],[2,0,2],[3,0,1],[4,3,1],[2,1,1]], threshold = 2)
#re =Solution().minMaxWeight(n = 2, edges = [[0,1,12]], threshold = 2)
#re =Solution().minMaxWeight(n = 3, edges = [[0,1,26],[1,0,35],[1,2,94]], threshold = 2)
#re =Solution().minMaxWeight(n = 4, edges = [[1,0,61],[2,0,31],[0,1,46],[3,0,67],[1,0,22]], threshold = 2)
#re =Solution().minMaxWeight(n = 4, edges =[[1,0,59],[3,0,43],[3,1,41],[1,3,6],[3,2,58],[2,0,76]], threshold = 3)
#re =Solution().minMaxWeight(n = 4, edges =[[3,0,64],[3,1,18],[1,3,82],[2,1,3]], threshold = 3)
print(re)