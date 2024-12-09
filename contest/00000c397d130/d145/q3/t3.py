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

def get_prime(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    return res
pls = get_prime(10**4)
pls = set(pls)
class Solution:
    def minOperations(self, n: int, m: int) -> int:
        if n in pls or m in pls:
            return -1
        k = len(str(n))
        g= [[] for _ in range(10**k)]
        for i in range(10**(k-1),10**k):
            if i in pls: continue
            for j in range(k):
                if str(i)[k-1-j] != "0":
                    g[i].append(i- 10**j)
                if str(i)[k-1-j] != "9":
                    g[i].append(i + 10**j)
        visit=[10**20]*20000

        cand=[(n,n)]
        while cand:
            c,a =heappop(cand)
            if visit[a] <=c:continue
            visit[a] = c
            for b in g[a]:
                if c+ b < visit[b]:
                    heappush(cand,(c+b,b))
                

        
        return visit[m] if visit[m] <10**20 else -1



re =Solution().minOperations(n = 10, m = 12)
print(re,85)
re =Solution().minOperations(n = 15, m = 88)
print(re,490)
re =Solution().minOperations(n = 7, m = 7)
print(re,490)