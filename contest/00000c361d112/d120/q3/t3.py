from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        left,right = 0,n-1
        for i in range(1,n):
            if nums[left]<nums[i]:
                left =i 
            else:
                break
        for i in range(n-2,-1,-1):
            if nums[i] < nums[right]:
                right = i 
            else:
                break
        if left >=right:
            return n*(n+1)//2
        #print(left,right)
        l = 0
        sm = 0
        for r in range(right,n):
            while nums[l]<nums[r] and l <= left:
                l +=1
            sm += l+1 
            #print(r,sm,l)
        sm +=left+1
        return sm +1





re =Solution().incremovableSubarrayCount([1])
print(re)