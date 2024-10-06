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

import itertools
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        ls =[bin(a)[2:] for a in nums]
        x =[1,2,0]
        ord2 = itertools.permutations(x)
        mx = 0 
        #print(ord)
        for a,b,c in ord2:
            t = ls[a] + ls[b] + ls[c]
            mx = max(mx,int("0b"+t ,2))
        return mx




re =Solution().maxGoodNumber([1,2,3])
print(re)