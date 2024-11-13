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
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        ret = 0
        dic =defaultdict(int)
        n = len(nums)
        for a in nums:
            dic[a]+=1
        for mid in nums:
            t= dic[mid]
            l= bisect_left(nums,mid-k)
            r = min(bisect_right(nums,mid+k),n-1)
            if nums[r] > mid+k:
                r-=1
            b = r-l-t+1
            ret = max(ret, t + min(b,numOperations))
            #print(ret,l,r,b,mid,t)
        l = 0
        for i,a in enumerate(nums):
            while a -2*k >nums[l]:
                l +=1
            ret = max(ret, min( i-l+1, numOperations) )
        return ret





re =Solution()
print(re)