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
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0 
        sl = SortedList([])
        dic = defaultdict(list)
        for i,a in enumerate(nums):
            if a == 0:
                sl.add(i)
            else:
                dic[a].append(i)
                cnt = cnt+1
        keys = list(dic.keys())
        keys.sort()
        for k in keys:
            ls = dic[k]
            m = len(ls)
            pre = -1 
            for a in ls:
                t =sl.bisect_left(a)
                if t == pre:
                    cnt -=1
                else:
                    pre =t
            for a in ls:
                sl.add(a)
        return cnt
        





re =Solution().minOperations([1,2,1,2,1,2])
print(re)