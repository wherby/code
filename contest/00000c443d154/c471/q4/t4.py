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

from collections import Counter
def getDecompositListUnderN(n):
    dic =[Counter() for _ in range(n+2)]
    visited=[False for _ in range(n+2)]
    dic[1][1] =0 ## ??
    for i in range(2,n+1):
        if visited[i]:
            continue
        dic[i][i] =0
        for j in range(i,n+1,i):
            t= j
            visited[j] =1
            while t%i ==0:
                dic[j][i] +=1
                t = t//i
    return dic
dls = getDecompositListUnderN(10**5)
class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        dic = {}
        for a in nums:
            if a not in dic:
                tl =[]
                for k,v in dls[a].items():
                    if v%2 != 0:
                        if k != 1:
                            tl.append(k)
                tl.sort()
                dic[a]=tuple(tl)
        acc =0
        curc = Counter()
        def dfs(a,p):
            nonlocal acc
            t1 = dic[nums[a]]
            acc +=curc[t1]
            curc[t1] +=1
            for b in g[a]:
                if b != p:
                    dfs(b,a)
            curc[t1] -=1
        dfs(0,-1)
        #print(dic)
        return acc





re =Solution().sumOfAncestors(n = 4, edges = [[0,1],[0,2],[1,3]], nums = [1,2,9,4])
print(re)