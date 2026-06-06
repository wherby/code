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
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mn = n*100

        def verify(a,b):
            cnt = 0 
            for i in range(n):
                t = nums[i]%k
                if i %2 ==0:
                    
                    cnt += min(abs((t-a)%k), k - abs((t-a)%k))
                else:
                    cnt += min(abs((t-b)%k), k - abs((t-b)%k))
            return cnt 
        for i in range(k):
            for j in range(k):
                if i != j :
                    mn = min(mn,verify(i,j))
        return mn





re =Solution().minOperations([38,75],11)
print(re)
print(38%11,75%11)