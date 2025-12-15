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
    def minMoves(self, balance: List[int]) -> int:
        if sum(balance)<0:
            return -1 
        n = len(balance)
        idx = -1 
        for i in range(n):
            if balance[i]<0:
                idx = i 
        if idx ==-1:
            return 0 
        toSum = -balance[idx]
        acc =0
        sm = 0
        #print(toSum)
        for i in range(1,n):
            l,r = (idx-i +n)%n, (idx+i)%n 
            if acc+balance[l] + balance[r] >= toSum:
                return  sm +(toSum -acc)*i 
            else:
                sm += i*(balance[l] + balance[r])
                acc += (balance[l] + balance[r])





re =Solution().minMoves([-2,4,4])
print(re)