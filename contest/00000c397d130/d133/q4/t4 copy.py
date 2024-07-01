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
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        mod = 10**9+7
        requirements.sort()
        sm = 0
        cnt = 1
        dic ={}
        dic[0]=1

        acc =1 
        lasta,lastb = 0,0
        for a,b in requirements:
            if b != lastb:
                c1 = las
                c2 = a - lasta
                acc =acc*math.comb(c2,c1)%mod
            else:
                pass
            lasta,lastb=a,b
        while lasta != n-1:
            print(lasta)
            acc =acc*(n-lasta)%mod
            lasta +=1
        return acc
        
             
        



re =Solution().numberOfPermutations(n = 3, requirements = [[2,2],[0,0]])
print(re)