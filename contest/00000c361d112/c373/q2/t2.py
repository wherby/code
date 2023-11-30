from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vl=set(['a','e','i','o','u'])
        acc = 0
        n = len(s)
        sm =0
        for l in range(n):
            acc =0
            for i,a in enumerate(s[l:]):
                if a in vl:
                    acc +=1
                else:
                    acc -=1
                #dic[acc] +=1
                if acc ==0 and ((i+1)//2)**2 %k==0:
                    sm +=1
        return sm
        
            





re =Solution().beautifulSubstrings(s = "baeyh", k = 2)
print(re)