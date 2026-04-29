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
    def minOperations(self, nums: list[int]) -> int:
        pre = 0
        cnt =0
        for a,b in pairwise(nums):
            if b >=a:
                continue 
            else:
                cnt += max(a-b,0)
                pre= max(a-b,pre)
                #print(a,b,cnt)
        return cnt
            





re =Solution().minOperations([3,3,2,1])
print(re)