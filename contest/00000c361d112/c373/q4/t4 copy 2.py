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
        m =2
        while (m//2) *(m//2)%k:
            m+=1
        k = m
        #k = k*2
        acc = 0
        sm =0
        dic = {}
        acc =0
        dic[0]=[0]*k
        dic[0][k-1] +=1
        #print(k)
        for i,a in enumerate(s):
            if a in vl:
                acc +=1
            else:
                acc -=1
            if acc not in dic:
                dic[acc] = [0]*k
            dic[acc][i%k] +=1
        for _,v in dic.items():
            for a in v:
                sm += a*(a-1)//2
        # acc =0 
        # print(sm)
        # for i,a in enumerate(s):
        #     if a in vl:
        #         acc +=1
        #     else:
        #         acc -=1
        #     dic[acc][i%k] -=1
        #     t = dic[acc][i%k]
        #     sm += t
        return sm
        
            





re =Solution().beautifulSubstrings("baeyh",2)
#re =Solution().beautifulSubstrings("uzuxpzou",3)
print(re)