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
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        n = len(colors)
        #g = [[] for _ in range(n)]
        
        dir = {"R":0,"B":1,"W":2}
        ind = [0]*n
        out = [0]*n
        for a,b in edges:
            oa = dir[colors[a]]
            ob = dir[colors[b]]
            
            if (oa-ob+3)%3 ==1:
                ind[a] +=1
                out[b] +=1
            elif (oa-ob+3)%3 ==2:
                ind[b]+=1 
                out[a] +=1
            else:
                return -1
            
        #     print(oa,ob,a,b,ind)
        # print(ind)
        if max(out) >2:
            return -1
        cand  =[]
        for a in range(n):
            if ind[a] ==0:
                cand.append(a)
        if len(cand) ==1:
            return cand[0]
        return -1
        





#re =Solution().findColoredRoot(edges = [[3,1],[3,2],[1,4],[2,0]], colors = "BRRWB")
#re =Solution().findColoredRoot(edges = [[1,0]], colors = "BB")
re = Solution().findColoredRoot([[0,1],[0,2],[0,3]],"RBBB")
print(re)