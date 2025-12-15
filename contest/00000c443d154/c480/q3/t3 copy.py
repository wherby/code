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
        if all(a>0 for a in balance):
            return 0
        n = len(balance)
        
        t1 = sum(balance) / n 
        pre = [balance[0]-t1]
        print(balance)
        balance = [a-t1 for a in balance]
        for a in balance[1:]:
            pre.append(pre[-1]+a)
        pre = pre[:-1]
        print(pre,t1)
        pre.sort()
        mid =-1
        if n%2 ==1:
            mid = pre[n//2]
        else:
            mid=pre[n//2 -1]

        return sum(abs(t-mid) for t in pre)




re =Solution().minMoves([-2,4,-2,4,-2,4,-2,4])
print(re)