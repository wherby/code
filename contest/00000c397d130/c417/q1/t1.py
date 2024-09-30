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
    def kthCharacter(self, k: int) -> str:
        s="a"
        while len(s)<k:
            s1 =[chr(ord(a)+1) for a in s]
            s = s+"".join(s1) 
            #print(s)
        return s[k-1]





re =Solution().kthCharacter(10)
print(re)