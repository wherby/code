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

class COMB:
    def __init__(self, n=100000, mod=1000000007):
        self.N = n
        self.mod = mod
        self.fac = [0] * self.N
        self.finv = [0] * self.N
        self.fac[0] =  1
        for i in range(1, self.N ):
            self.fac[i] = self.fac[i - 1] * i % self.mod
        self.finv[-1] = pow(self.fac[-1],-1,self.mod)
        for i in range(self.N-1,0,-1):
            self.finv[i-1] = self.finv[i ] *i % self.mod

    def C(self, n, m):
        return self.fac[n] * self.finv[n - m] % self.mod * self.finv[m] % self.mod

    def A(self, n, m):
        return self.fac[n] * self.finv[n - m] % self.mod
comb = COMB(10**5)
class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        mod = 10**9+7
        
        return comb.C(n-1,k)*2%mod





re =Solution().countVisiblePeople(37,26,11)
print(re)