# https://leetcode.com/contest/weekly-contest-493/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from pyparsing import nums
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        left = [0] * n
        left[0] = 1
        for i in range(1, n):
            if i >= 2 and nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 2
        right = [0] * n
        right[n-1] = 1
        for i in range(n-2, -1, -1):
            if i <= n-3 and nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
                right[i] = right[i+1] + 1
            else:
                right[i] = 2
        ans = min(max(left),n-1) +1
        for i in range(1, n-1):
            diff = nums[i+1] - nums[i-1]
            if diff % 2 == 0: 
                d = diff // 2
                
                if (i-1 >= 0 and i+1 < n and left[i-1] >= 2 and right[i+1] >= 2 and
                    nums[i-1] - nums[i-2] == d and nums[i+2] - nums[i+1] == d):
                    ans = max(ans, left[i-1] + 1 + right[i+1])
                
                if i-1 >= 0 and left[i-1] >= 2 and nums[i-1] - nums[i-2] == d:
                    if i+1 < n:
                        ans = max(ans, left[i-1] + 2)  
                if i+1 < n and right[i+1] >= 2 and nums[i+2] - nums[i+1] == d:
                    if i-1 >= 0:
                        ans = max(ans, 2 + right[i+1])  
    
        
        return ans




re =Solution().longestArithmetic([19334,19334,24488,58213,19334,19334,19334,19334,19334,19334])
print(re)