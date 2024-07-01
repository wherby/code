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
    def minOperations(self, nums: List[int]) -> int:
        n =len(nums)
        cnt =0
        for i in range(n-2):
            if nums[i]%2 ==0:
                nums[i+1] +=1
                nums[i+2] +=1
                cnt +=1
        if nums[n-1]%2 ==1 and nums[n-2] %2 ==1:
            return cnt 
        return -1 





re =Solution()
print(re)