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
from math import sqrt

from math import sqrt

def getAllDiv(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    def getAllComb(pls,n):
        ret =[]
        for p in pls:
            while n%p ==0:
                ret.append(p)
                n = n//p 
        return ret
    allC = getAllComb(res,n)
    ret =set([])
    for i in range(2<<len(allC)):
        acc =1
        for j in range(len(allC)):
            if (1<<j) &i :
                acc *= allC[j]
        ret.add(acc)
    return ret
        
import itertools
class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        ls = getAllDiv(n)

        ret = [1]*k
        ret[0] = n
        tmp =[]
        def dfs(res,idx):
            nonlocal ret,tmp
            if idx == 0 and res ==1 :
                if max(tmp)-min(tmp)< max(ret) - min(ret):
                    ret = list(tmp)
                return 
            if idx == 0:
                return 
            for a in ls:
                if res %a == 0:
                    tmp.append(a)
                    dfs(res//a,idx-1)
                    tmp.pop()
        dfs(n,k)
        return ret





re =Solution().minDifference(360,4)
print(re)