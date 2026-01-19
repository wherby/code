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


vowls=set(['a', 'e', 'i', 'o',  'u'])
        

class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        a,b = 0,0 
        for c in s:
            if c in vowls:
                a +=1
            elif c.isalpha():
                b +=1 
        return a //b if b >0 else 0





re =Solution()
print(re)