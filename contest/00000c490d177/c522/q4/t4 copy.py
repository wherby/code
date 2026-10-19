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

class Solution:
    def countGoodStrings(self, n: int) -> int:
        MOD = 10**9 + 7
        def mat_mul(A, B):
            return [
                [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
                 (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
                [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
                 (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
            ]
        
        def mat_pow(M, p):
            res = [[1, 0], [0, 1]]
            while p > 0:
                if p & 1:
                    res = mat_mul(res, M)
                M = mat_mul(M, M)
                p >>= 1
            return res
        if n == 1:
            fib_n = 1
        else:
            M = [[1, 1], [1, 0]]
            Mn = mat_pow(M, n - 1)
            fib_n = Mn[0][0]
        
        return (2 * fib_n) % MOD



re =Solution().countGoodStrings(4)
print(re)