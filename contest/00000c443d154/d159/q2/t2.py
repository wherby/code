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
    def maxArea(self, coords: List[List[int]]) -> int:
        dicx = defaultdict(list)
        dicy = defaultdict(list)
        minx=maxx = coords[0][0]
        miny=maxy = coords[0][1]
        for x,y in coords:
            dicx[x].append(y)
            dicy[y].append(x)
            minx  = min(minx,x)
            maxx = max(maxx,x)
            miny = min(miny,y)
            maxy = max(maxy,y)
        ret = 0 
        for x in dicx.keys():
            ls = list(dicx[x])
            ls.sort()
            ret = max(ret,(ls[-1]-ls[0]) *max(abs(x-minx),abs(x-maxx)))
        for y in dicy.keys():
            ls = list(dicy[y])
            ls.sort()
            ret = max(ret,(ls[-1]-ls[0]) *max(abs(y- miny),abs(y-maxy)))
        return ret if ret != 0 else -1
        





re =Solution().maxArea([[1,1],[1,2],[3,2],[3,3]])
print(re)