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
from functools import reduce
from operator import xor
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9+7
        for l,r,k,v in queries:
            for j in range(l,r+1,k):
                nums[j] = (nums[j]*v)%mod
        return reduce(xor,nums)




re =Solution().xorAfterQueries( nums = [1,1,1], queries = [[0,2,1,4]])
print(re)