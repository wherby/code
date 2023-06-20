# OT
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue

def allState(k,m):
    ret=[]
    state = (1<<k) -1
    while (state <(1<<m)):
        ret.append(state)
        c = state &(-state)
        r = state +c
        state= (((r ^ state) >>2)//c) |r 
    return ret

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        ind = [0]*n
        g = [[] for _ in range(n)]
        for a,b in relations:
            g[a-1].append(b-1)
            ind[b-1] +=1
        mx = n 
        msks  = allState(k,n)
        @cache
        def dfs(status,acc):
            nonlocal mx
            if acc>= mx:return
            if status == (1<<n) -1:
                mx = min(mx,acc)
                return acc
            for msk in msks:
                tls = []
                for i in range(n):
                    if (1<<i) & msk and (1<<i)&status ==0 and ind[i]==0:
                        tls.append(i)
                if len(tls)>0:
                    k =0 
                    for a in tls:
                        k+= 1<<a 
                        for b in g[a]:
                            ind[b] -=1
                    dfs(status + k ,acc +1)
                    for a in tls:
                        for b in g[a]:
                            ind[b] +=1
        dfs(0,0)
        return mx

re = Solution().minNumberOfSemesters(n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2)
print(re)