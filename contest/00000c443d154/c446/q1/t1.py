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
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n= len(instructions)
        visit ={}
        c = 0
        acc =0
        while c not in visit and 0<=c <n:
            visit[c] = 1
            if instructions[c] == "jump":
                c = c+values[c]
            else:
                
                acc += values[c] 
                c = c+1
        return acc





re =Solution()
print(re)