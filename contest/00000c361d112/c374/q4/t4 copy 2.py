from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf
mod = 10**9 +7
def quickPow(x,y):
    ret =1
    cur = x 
    while y >0:
        if y & 1:
            ret = ret * cur % mod
        cur = cur *cur % mod
        y = y //2
    return ret

def inv(x):
    return quickPow(x,mod-2)
def comb2(n,m, mod= 10**9+7):
    cnt = 1
    acc =1
    for i in range(m):
        cnt *=(n-i) %mod
        acc *= (i+1)%mod
    cnt = cnt* inv(acc)%mod
    return cnt
MOD = 10**9+7
MX = 10**5
class Factorial:
    def __init__(self, MX):
        self.f = [1] * (MX + 1)
        self.g = [1] * (MX + 1)
        for i in range(1, MX+1):
            self.f[i] = self.f[i-1] * i % MOD
        self.g[-1] = pow(self.f[-1], MOD-2, MOD)
        for i in range(MX-1, -1, -1):
            self.g[i] = self.g[i+1] * (i+1) % MOD

    def fact(self, n):
        return self.f[n]

    def fact_inv(self, n):
        return self.g[n]

    def perm(self, n, m):
        if m < 0 or n < 0 or n < m: return 0
        return self.f[n] * self.g[n-m] % MOD

    def comb(self, n, m):
        if m < 0 or n < 0 or n < m: return 0
        return self.f[n] * self.g[m] * self.g[n-m] % MOD

    def catalan(self, n):
        return (self.comb(2*n, n) - self.comb(2*n, n-1)) % MOD

    def inv(self, n):
        return self.f[n-1] * self.g[n] % MOD

fact = Factorial(MX)


class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        mod = 10**9+7
        sick.sort()
        d,s = [],[]
        m = len(sick)
        for i in range(1,m):
            d.append(sick[i]-sick[i-1]-1)
        if sick[0] != 0:
            s.append(sick[0])
        if sick[-1] != n-1:
            s.append(n-1- sick[-1])
        ret = 1
        #print(d,s)
        d = [a for a in d if a !=0]
        ds = sum(d) -len(d)
        #print(ds,d)
        cnt1 = sum(d) + sum(s)
        ads = d+s
        for a in ads:
            ret = ret* fact.comb(cnt1,a)
            cnt1 -=a
        ret = ret * quickPow(2,ds)%mod
        return ret %mod
        
        





re =Solution().numberOfSequence(100000,[2510,3199,3918,4487,8785,9266,14154,15449,22538,28707,32831,33117,37673,38416,44485,47577,49248,50147,60773,66823,80580,82775,84330,87851,87953,89189,91514,92517,97026])
#re = Solution().numberOfSequence(5,[0,1,4])
print(re)