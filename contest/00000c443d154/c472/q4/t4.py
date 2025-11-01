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
    def longestBalanced(self, nums: List[int]) -> int:
        diclst = defaultdict(int)
        acc =0
        dp =[0]*2
        vis={}
        blanced={}
        blanced[0] = -1
        for i,a in enumerate(nums):
            b = a%2
            if a not in vis:
                if b :
                    acc +=1
                else:
                    acc -=1
            if a not in diclst:
                diclst[a] =i
            else:
                i1 = diclst[a]
                for k,v in blanced.items():
                    if v < i1
            




re =Solution()
print(re)