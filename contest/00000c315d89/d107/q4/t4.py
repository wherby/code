from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        dic = defaultdict(int)
        logs = [(b,a) for a,b in logs]
        logs.sort()
        qls = []
        for i,q in enumerate(queries):
            qls.append((q,i))
        qls.sort()
        m = len(logs)
        ret =[-1]*len(queries)
        left = 0
        li = 0
        for q,idx in qls:
            qs= q-x
            while li < m and logs[li][0]<= q:
                lt,ls = logs[li]
                dic[ls] +=1
                li +=1
            while left<m and logs[left][0]<qs:
                lt,ls = logs[left]
                dic[ls] -=1
                if dic[ls] ==0:
                    del dic[ls]
                left +=1
            ret[idx] = n- len(dic)
        return ret





re =Solution().countServers(n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11])
print(re)