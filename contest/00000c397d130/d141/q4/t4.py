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



class Comb():
    def __init__(self,m,n) -> None:
        self.comb =[[0]*(n+1) for i in range(m+1)]
        self.mod = 10**9+7

    def getComb(self,m,n):
        if self.comb[m][n] !=0:
            return self.comb[m][n]
        if n > m-n:
            return self.getComb(m,m-n)
        if n ==0: return 1
        if n==1: return m
        a = self.getComb(m-1,n-1)
        b =self.getComb(m-1,n)
        self.comb[m][n] = (a+b) %self.mod
        return self.comb[m][n]


comb = Comb(1000,1000)


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


class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        mod = 10**9+7
        acc =0
        ls = [1]
        for i in range(2,1001):
            ls.append(i*ls[-1]%mod)
        for i in range(1,min(x,n)+1):
            c = comb.getComb(x,i)*ls[i-1]
           
            t = c *(quickPow(i,n)- quickPow(i-1,n) )*quickPow(y,i)
            print(i,c,t,comb.getComb(n-1,i-1),quickPow(i,n-i),ls[i-1])
            acc = (acc+t)%mod
        return acc






re =Solution().numberOfWays(n = 3, x = 3, y = 4)
print(re)