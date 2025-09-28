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


MOD = 1_000_000_007

# a @ b，其中 @ 是矩阵乘法
def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    return [[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*b)]
            for row in a]

# a^n @ f0
def pow_mul(a: List[List[int]], n: int, f0: List[List[int]]) -> List[List[int]]:
    res = f0
    while n:
        if n & 1:
            res = mul(a, res)
        a = mul(a, a)
        n >>= 1
    return res

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9+7
        m = r-l +1
        idp = [0]*2*m
        mxt = [[0]*(m*2) for _ in range(m*2)]
        for i in range(m):
            for j in range(m):
                if i>j:
                    mxt[i][j+m]  =1
                if i<j:
                    mxt[i+m][j] =1
        for i in range(m):
            idp[i] =i 
            idp[m+i] = m-1-i
        #print(mxt)
        f0 = [[1] for _ in range(2*m)]
        mxt = pow_mul(mxt,n-2,f0)
        acc = 0
        for i in range(2*m):

            acc += mxt[i][0]*idp[i]
            acc %=mod 
        return acc
        





re =Solution().zigZagArrays(3,1,3)
print(re)