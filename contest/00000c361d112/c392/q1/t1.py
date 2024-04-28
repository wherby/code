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
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mx = 1 
        for l in range(2,n+1):
            for b in -1,1:
                
                for i in range(n-l+1):
                    isG = True
                    for j in range(i+1,i+l):
                        if (nums[j]-nums[j-1])*b <= 0:
                            isG = False
                    #print(l,isG,i,b)
                    if isG:
                        mx = max(mx,l)
                        #print(l,isG,i,b)
        return mx




re =Solution().longestMonotonicSubarray(  [1,1,5])
print(re)