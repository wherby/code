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
    def minFlips(self, s: str) -> int:
        mx = len(s)
        state = 0
        cnt =0
        for a in s:
            if a =="0" and state ==0:
                state =1
            elif a =="1":
                if state ==1:
                    state =2
                else:
                    cnt +=1
        mx = min(mx,cnt)
        cnt =state = 0
        for a in s:
            if a =="1":
                if state <2:
                    state +=1
            elif a =="0":
                if state ==2:
                    cnt +=1
        mx= min(mx,cnt)
        return mx
            





re =Solution()
print(re)