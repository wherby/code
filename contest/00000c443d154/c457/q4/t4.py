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
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        if sx == 0 and sy == 0 and ((sx!=tx) or (sy != ty)):
            return -1
        @cache
        def dfs(sx,sy):
            if sx ==tx and sy ==ty:
                return 0 
            mx = max(sx,sy)
            if sx != tx and  sx +mx >=tx:
                return dfs(tx,sy) +1
            if sy != ty and sy + mx >= ty:
                return dfs(sx,ty) +1
            if sx >= sy and tx >=sx+mx:
                return dfs(sx+mx,sy) +1
            if sx < sy and ty >=sy+mx:
                return dfs(sx,sy+mx)+1
            ret = 10**10
            if sx + mx <= tx:
                ret = min(ret,dfs(sx+mx,sy)+1)
            if sy + mx <= ty:
                ret = min(ret,dfs(sx,sy+mx)+1)
            return ret
        return dfs(sx,sy)



re =Solution().minMoves(sx = 0, sy = 1, tx = 2, ty = 3)
print(re)