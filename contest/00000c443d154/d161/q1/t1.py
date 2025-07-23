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


def get_prime(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    return res
ps = set(get_prime(10**5+3))
class Solution:
    def splitArray(self, nums: List[int]) -> int:
        acc1,acc2 = 0,0 
        for i,a in enumerate(nums):
            if i in ps:
                acc1 +=a 
            else:
                acc2 +=a 
        return acc1 -acc2





re =Solution()
print(re)