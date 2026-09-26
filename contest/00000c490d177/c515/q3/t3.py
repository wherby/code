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
    def maximumGap(self, skill: str, station: str) -> int:
        n = len(skill)
        m = len(station)
        
        def match(sks,sta):
            ret = [m]*n
            cs = 0
            
            for i in range(m):
                if sks[cs] == sta[i]:
                    ret[cs] = i 
                    cs +=1
                if cs ==n:
                    return ret

        pre = match(skill,station)
        pos = match(skill[::-1],station[::-1])
        mx = 0
        for i in range(n-1):
            mx = max(mx,m-pre[i]-1 - pos[n-2-i])
        return mx
            



re =Solution().maximumGap(skill = "aa", station = "aaaa")
print(re)