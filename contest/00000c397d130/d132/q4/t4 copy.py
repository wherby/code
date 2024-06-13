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
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dic = defaultdict(int)
        mx = 0
        dick = defaultdict(int)
        for a in nums:
            for j in range(k,-1,-1):
                dic[(a,j)] = max(dic[(a,j)]+1,dick[j-1]+1 )
                dick[j] = max(dick[j], dic[(a,j)])
                mx = max(mx,dic[(a,j)])
        #print(dic,dick)
        return mx 

        





re =Solution().maximumLength(nums = [1,2,1,1,3], k = 0)
print(re)