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
    def minOperations(self, queries: List[List[int]]) -> int:
        ls = [1,4]
        for i in range(20):
            ls.append(ls[-1]*4)
        def getN(x):
            k=bisect_right(ls,x)
            acc =0 
            for i in range(k-1,-1,-1):
                acc += (x-ls[i]+1)#*(i*2+1)
            return acc 
        ret = 0
        for a,b in queries:
            ret += (getN(b) - getN(a-1)+1)//2
            #print(ret,getN(b) - getN(a-1),getN(b) , getN(a-1))
        return ret




re =Solution().minOperations([[2,6]])

print(re)