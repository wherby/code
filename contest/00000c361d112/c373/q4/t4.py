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
        sm =0
        dic = defaultdict(deque)
        acc =0
        dic[0].append(-1)
        for i,a in enumerate(s):
            if a in vl:
                acc +=1
            else:
                acc -=1
            dic[acc].append(i)
        ls = [0]*10**5*3
        bcc = 0
        
        for i in range(1,10**5*3):
            if i*i%k==0:
                bcc +=1
            ls[i] = bcc
        # for k,v in dic.items():
        #     if k ==0:
        #         m = v[-1] -v[0]
        #         sm += ls[m//2]
        #print(sm,dic)
        acc =0
        for i,a in enumerate(s):
            if a in vl:
                acc +=1
            else:
                acc -=1
            dic[acc].popleft()
            if len(dic[acc]):
                print(dic[acc])
                t = dic[acc][-1] -dic[acc][0]
                sm +=ls[t//2]
        return sm
        
            





#re =Solution().beautifulSubstrings(s = "abba", k = 1)
re =Solution().beautifulSubstrings("uzuxpzou",3)
print(re)