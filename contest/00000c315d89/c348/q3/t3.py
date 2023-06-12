from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        m = len(queries)
        dic ={}
        qs =[]
        for t,idx,v  in reversed(queries):
            if (t,idx) not in dic:
                dic[(t,idx)] =1
                qs.append([t,idx,v])
            else:
                pass
        cs,rs = 0,0
        acc = 0
        for t,idx,v in reversed(qs):
            if t ==0:
                cs +=v
                acc += n*v -rs
            else:
                rs +=v 
                acc += n*v -cs
        return acc
            



re =Solution().matrixSumQueries(n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]])
print(re)