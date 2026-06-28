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
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        pls = [0]
        n = len(nums)
        for a in nums:
            pls.append(pls[-1] + a )
        cnt =0
        for i in range(n):
            for j in range(i+1,n+1):
                t = pls[j] - pls[i]
                st = str(t)
                if st[0]==str(x) and st[-1]==str(x):
                    cnt+=1 
        return cnt





re =Solution().countValidSubarrays(nums = [1,100,1], x = 1)
print(re)