from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
from itertools import pairwise
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

    def closestPrimes(self, left: int, right: int) -> List[int]:
        pls = get_prime(right)
        pls= list(pls)
        pls.sort()
        l = bisect_left(pls,left)
        idx = l 
        ret =[]
        while idx < len(pls) and pls[idx]<=right:
            ret.append(pls[idx])
            idx +=1
        if len(ret) <2:
            return [-1,-1]
        res = [ret[0],ret[1]]
        mx = ret[1]-ret[0]
        for i in range(len(ret)-1):
            if ret[i+1] - ret[i] < mx:
                mx = ret[i+1]-ret[i]
                res =  [ret[i],ret[i+1]]
        return res
        





re =Solution().closestPrimes(10,19)
print(re)