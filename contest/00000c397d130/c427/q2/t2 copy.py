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
                k3 = sl.bisect_left((a,k))
                k4 = sl.bisect_left((b,k))
                if (a,b) in cand:
                    cp = cand[(a,b)]
                    k1 = sl.bisect_left(cp[0])
                    k2 = sl.bisect_left(cp[1])
                    
                    #print(k3-k1,k4-k2,k1,k2,k3,k4,sl, odic[(a,b)],k2-k1)
                    if k3-k1 ==k4-k2 and odic[(a,b)] +1==k2-k1:
                        ret = max(ret,(b-a)*(k -cp[0][1]))
                
                cand[(a,b)] = ((a,k),(b,k))
                odic[(a,b)] = k4-k3
            for a in s1:
                t1 = sl.bisect_left((a,k))
                
                sl.add((a,k))
                #print(k,a,b,sl)
        return ret 
                





re =Solution().maxRectangleArea( points = [[94,39],[34,56],[94,56],[34,39],[14,46]])
print(re,1020)
re =Solution().maxRectangleArea( points = [[33,92],[98,100],[33,100],[98,92],[42,100]])
print(re,-1)
re =Solution().maxRectangleArea( points = [[1,1],[1,3],[3,1],[3,3],[2,2]])
print(re,-1)