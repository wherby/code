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
from itertools import pairwise

class Comb():
    def __init__(self,m,n) -> None:
        self.comb =[[0]*(n+1) for i in range(m+1)]
        self.mod = 10**9+7

    def getComb(self,m,n):
        if n>m:return 0
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



comb = Comb(100000,100)

from collections import Counter
class Solution:
    def minMaxSums(self, nums: List[int], kk: int) -> int:
        nums.sort()
        mod = 10**9+7
        ret = 0
        n = len(nums)
        for i,a in enumerate(nums):
            for k1 in range(1,kk+1):
                ret += comb.getComb(i,k1-1)*a
                ret += comb.getComb(n-i-1,k1-1)*a
            #print(k,ret)
        return ret %mod

        




re =Solution().minMaxSums(nums = [1,2,3], kk = 2)

#re =Solution().minMaxSums(nums = [5,0,6], kk = 1)
print(re)