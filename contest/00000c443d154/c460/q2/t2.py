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
    def numOfSubsequences(self, s: str) -> int:
        def getCnt(s):
            sl=[[] for _ in range(3)]
            dic= {"L":0,"C":1,"T":2}
            for i,a in enumerate(s):
                if a in dic:
                    sl[dic[a]].append(i)
            cnt = 0 
            m2 = len(sl[2])
            for a in sl[1]:
                idx1 =bisect_left(sl[0],a)
                idx2 = bisect_left(sl[2],a) 
                cnt += idx1 * (m2-idx2)
            return cnt
        ret = 0 
        ret = getCnt("L" +s)
        ret = max(ret, getCnt(s+"T"))
        re1 = getCnt(s)
        sl=[[] for _ in range(3)]
        dic= {"L":0,"C":1,"T":2}
        for i,a in enumerate(s):
            if a in dic:
                sl[dic[a]].append(i)
        def getMX(l1,l2):
            mx =0 
            m = len(l2)
            for i,a in enumerate(l1):
                idx = bisect_left(l2,a)
                mx = max(mx,(i+1)*(m-idx))
            return mx
        slr0 = [-a for a in sl[0]]
        slr2 =[-a for a in sl[2]]
        def getMX2(l1,l2):
            mx = 0 
            m = len(l2)
            for i,a in enumerate(l2):
                idx = bisect_left(l1,a)
                mx = max(mx,idx*(m-i))
            return mx
        #print(ret,re1,slr0,slr2,getMX(sl[0],sl[2]),getMX(slr2,slr0),getMX2(sl[0],sl[2]))
        ret = max(ret,re1 + getMX(sl[0],sl[2]),re1 + getMX2(sl[0],sl[2]))
        return ret



        




re =Solution().numOfSubsequences("LCTKLCLT")
print(re)