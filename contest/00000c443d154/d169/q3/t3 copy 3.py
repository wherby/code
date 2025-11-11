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


from math import ceil, log2
 

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mx = 0 
        if n <=1:
            return n 
        left = [1]*n 
        for i in range(1,n):
            if nums[i]>=nums[i-1]:
                left[i] = left[i-1]+1 
        right = [1]*n 
        for i in range(n-2,-1,-1):
            if nums[i]<= nums[i+1]:
                right[i] = right[i+1]+1
        mx = max(left)
        for i in range(n):
            if i == 0:
                mx =max(mx,1+ right[1])
            elif i == n-1:
                mx = max(mx,left[n-2]+1)
            else:
                if nums[i-1]<= nums[i+1]:
                    mx = max(mx,left[i-1] + 1 + right[i+1])
                mx = max(mx,left[i-1] +1, 1+ right[i+1])
            if i < n-2 and nums[i] <= nums[i+2]:
                mx = max(mx,left[i] + 1 + right[i+2])
        return mx



re =Solution().longestSubarray( nums =[9,9,0,4,9])
print(re)