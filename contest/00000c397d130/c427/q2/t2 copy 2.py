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
from itertools import pairwise
class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        ret = -1 
        dic = defaultdict(list)
        for a,b in points:
            dic[a].append(b)
        keys = list(dic.keys())
        keys.sort()
        sl = SortedList([])
        cand={}
        #print(dic)
        odic={}
        for k in keys:
            s1 = dic[k]
            s1.sort()
            for a,b in pairwise(s1):
                if (a,b) in cand:
                    k1= cand[(a,b)]
                    isG = True
                    for x,y in points:
                        if k1<x<k and  a<=y<=b:
                            isG =False
                            #print(x,y,a,b)
                    if isG:
                        ret = max(ret,(b-a)*(k-k1))
                cand[(a,b)] = k
                #print(cand)
        return ret 
                





re =Solution().maxRectangleArea( points = [[94,39],[34,56],[94,56],[34,39],[14,46]])
print(re,1020)
re =Solution().maxRectangleArea( points = [[33,92],[98,100],[33,100],[98,92],[42,100]])
print(re,-1)