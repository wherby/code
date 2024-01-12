from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hs: List[int], vs: List[int]) -> int:
        mod = 10**9+7
        hls = [1]+hs+[m]
        vls = [1] + vs +[n]
        hls.sort()
        vls.sort()
        hdic={}
        vdic={}
        if len(hls)> len(vls):
            hls,vls = vls,hls 
        t = len(hls)
        for i in range(1,t):
            for j in range(i):
                hdic[hls[i]-hls[j]] = 1 
        t = len(vls)
        for i in range(1,t):
            for j in range(i):
                vdic[vls[i]-vls[j]] = 1 
        keys = list(hdic.keys())
        keys.sort(reverse= True)
        #print(keys,vdic)
        for k in keys:
            if k in vdic:
                return k*k%mod 
        return -1
        
        





re =Solution().maximizeSquareArea( 3,9,[2],[8,6,5,4])
print(re)