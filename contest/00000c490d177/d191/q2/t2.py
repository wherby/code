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
    def countSpecialIntegers(self, nums: list[int]) -> int:
        dic = defaultdict(list)
        for i,a in enumerate(nums):
            dic[a].append(i)
        cnt = 0
        for k,v in dic.items():
            if len(v) >= 3 :
                isG = True
                d = v[1]-v[0]
                for a,b in pairwise(v):
                    if a+d !=b:
                        isG = False
                if isG:
                    cnt +=1
        return cnt





re =Solution()
print(re)