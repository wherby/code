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
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        s3,s1 = "0",0
        pre = [("0",0)] 
        mod = 10**9+7
        for i,a in enumerate(s):
            if int(a) != 0:
                s3 +=a 
                s1 += int(a)
            pre.append((s3,s1))
        ret = []
        
        #print(pre)
        for a,b in queries:
            p1,p2 = pre[a],pre[b+1]
            s1,s2 = p1
            t = len(p1[0])
            c = int("0" +p2[0][t:]) 
            d = p2[1] -p1[1] 
            #print(c,d)
            ret.append(c*d%mod)
        return ret





re =Solution().sumAndMultiply(s = "10203004", queries = [[0,7],[1,3],[4,6]])
print(re)