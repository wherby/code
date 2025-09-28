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
    def distinctPoints(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        x,y = 0,0 
        def getDiff(ch):
            x,y = 0,0
            if ch == "U":
                y +=1
            elif ch == "D":
                y -=1
            elif ch == "L":
                x -=1
            else:
                x +=1
            return (x,y)
        for i in range(k-1):
            dx,dy = getDiff(s[i])
            x ,y = x+dx,y+dy 
        n = len(s)
        for i in range(k-1,n):
            if i >=k:
                dx,dy = getDiff(s[i-k])
                x ,y = x-dx,y-dy 
            dx,dy = getDiff(s[i])
            x ,y = x+dx,y+dy 
            dic[(x,y)] +=1
        return len(dic)
            




re =Solution().distinctPoints(s = "UDLR", k = 4)
print(re)