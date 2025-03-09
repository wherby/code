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
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:

        def merge(x1,y1,x2,y2):
            if x1 >x2:
                return merge(x2,y2,x1,y1)
            if x2 >y1 or x1>y1 or x2>y2:
                return (x1,x1-1)
            return (x2,min(y1,y2))
        
        x1,y1 = bounds[0][0],bounds[0][1]
        o0 = original[0]

        for o,b in zip(original[1:],bounds[1:]):
            x2,y2 = b[0] -o +o0,b[1] - o +o0 
            #@print(x1,y1,x2,y2)
            nx,ny = merge(x1,y1,x2,y2)
            x1,y1 = nx,ny
            #print(x1,y1,o,b)
        return  max(0, y1-x1+1)






re =Solution().countArrays(original = [1,2,3,4], bounds = [[1,2],[2,3],[3,4],[4,5]])
print(re)