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
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        mod = 10**9+7
        idx = 0
        dic =defaultdict(int)
        dic2 = defaultdict(list)
        for i,a in enumerate(nums):
            if a not in dic:
                idx +=1
            dic[a] +=1
            dic2[a].append(i)
        print(dic,dic2)
        pre= [[0]*idx]
        for a in nums:
            t = list(pre[-1])
            t[dic[a]] +=1
            pre.append(t)
        
        def calc(ls):
            if len(ls)>4:
            if len(ls)>4:


        for k in range(dic.keys()):







re =Solution().subsequencesWithMiddleMode([1,2,2,3,3,4])
print(re)