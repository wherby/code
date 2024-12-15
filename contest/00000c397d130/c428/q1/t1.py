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
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        mx = 0
        ret =-1
        
        events= [(0,0)] +events
        n = len(events)
        for i in range(1,n):
            b = events[i][1] -events[i-1][1]
            if b >mx:
                mx =b 
                ret =events[i][0]
            if b ==mx and ret >events[i][0]:
                ret = events[i][0]
            #print(ret,mx,i)
        return ret






re =Solution().buttonWithLongestTime(events = [[1,2],[2,5],[3,9],[1,15]])
print(re)