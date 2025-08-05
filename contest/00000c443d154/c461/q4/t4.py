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
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)

        
        inc = [float('-inf')] * n
        dec = [float('-inf')] * n
        inc2 = [float('-inf')] * n
        
        for i in range(1, n):
            # Update inc[i]
            if nums[i] > nums[i - 1] :
                inc[i] = max( inc[i - 1] + nums[i], nums[i-1]+nums[i]) 
            
            # Update dec[i]
            if nums[i] < nums[i - 1] :# and state >0:
                dec[i] = max(dec[i-1]+nums[i], nums[i]+inc[i-1])

            if nums[i] > nums[i - 1] :
                inc2[i] = max(inc2[i-1] + nums[i],nums[i]+dec[i-1] )
            #print(inc,dec,inc2)
            #print(i,nums[i],state, nums[i] > nums[i - 1] ,state >1,nums[i-1]+nums[i]+dec[i-1])
        max_sum = max(inc2)
        return max_sum 



re =Solution().maxSumTrionic([0,-2,-1,-3,0,2,-1])
print(re)