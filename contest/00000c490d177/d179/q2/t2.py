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
class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        mod = 10**9+7
        return comb2(n-1,k)*2%mod





re =Solution().countVisiblePeople(37,26,11)
print(re)