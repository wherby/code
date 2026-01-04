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
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        restrictions = [[0,0]] + restrictions
        restrictions.sort()
        
        mx=0
        def getMx(st,ed,arr):

            sm = sum(arr)
            cur = st
            ret = cur
            for a in arr:
                cur +=a 
                if cur <=ed +sm - (cur-st):
                    ret =max(ret, cur )
            #print(sm,ret,st,ed,arr)
            return ret 
        cur = 0
        for s1,ed1 in pairwise(restrictions):
            stidx,st = s1 
            edidx,ed = ed1 
            st =min(st,cur)
            if cur + sum(diff[stidx:edidx]) < ed:
                ed = st + sum(diff[stidx:edidx])
            mx = max(mx,getMx(cur,ed,diff[stidx:edidx]))
            cur = ed
        mx = max(mx,cur + sum(diff[restrictions[-1][0]:]))
        return mx






re =Solution().findMaxVal(n = 10, restrictions = [[3,1],[8,1]], diff = [2,2,3,1,4,5,1,1,2])
re =Solution().findMaxVal(n = 2, restrictions = [[1,15]], diff = [2])
print(re)