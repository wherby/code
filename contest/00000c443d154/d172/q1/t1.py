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
        dic = defaultdict(list)
        for i,a in enumerate(nums):
            dic[a].append(i+1)
        mx = 0 
        for a,vs in dic.items():
            if len(vs)>1:
                mx = max(mx,vs[-2])
        return (mx+2)//3





re =Solution().minOperations([1,2,3,2,3,1,2])
print(re)