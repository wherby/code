from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res =[]
        for i,(a,b,c,d) in enumerate(variables):
            acc = 1 
            for _ in range(b):
                acc = acc*a%10
            acc =acc%d
            a = acc
            #print(i,a)
            for _ in range(c-1):
                acc = acc*a %d 
            #print(acc)
            if acc == target:
                res.append(i)
        return res





re =Solution().getGoodIndices(variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2)
print(re)