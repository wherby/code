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

class Solution(object):
    def sortPermutation(self, nums):
        ls=[]
        for i,a in enumerate(nums):
            if a != i:
                ls.append(a)
        if len(ls)==0:
            return 0 
        acc = ls[0]
        for a in ls:
            acc =acc&a 
        return acc




re =Solution()
print(re)