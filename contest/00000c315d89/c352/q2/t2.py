from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

def get_prime(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    return res

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        pls = get_prime(n+1)
        pls = set(pls)
        ret =[]
        for i in range(2,n+1):
            if i in pls and n-i>=i and n-i in pls:
                ret.append([i,n-i])
        return ret



re =Solution()
print(re)