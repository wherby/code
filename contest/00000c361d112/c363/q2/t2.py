from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        sm = 0 
        n = len(nums)
        if nums[0] >0:
            sm +=1
        
        for i,a in enumerate(nums):
            if i != n-1:
                if a <i+1 and nums[i+1]> i+1:
                    sm +=1
            else:
                if a <n:
                    sm+=1
        return sm
            
        




re =Solution().countWays(nums = [6,0,3,3,6,7,2,7])
print(re)