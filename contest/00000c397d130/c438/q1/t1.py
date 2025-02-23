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
from itertools import pairwise
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(a) for a in s]
        while len(s)>2:
            t=[]
            for a,b in pairwise(s):
                c = (a+b)%10
                t.append(c)
            s= t 
        return s[0] == s[1]





re =Solution().hasSameDigits("4802870269162891409411160836125514611")
print(re)