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
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        sm = sum(nums)
        nums.sort(reverse=True)
        n = len(nums)

        @cache
        def dfs(i,op1,op2):
            if i == n :
                return 0
            ret = 0
            if op1:
                ret = max(ret,nums[i]//2 + dfs(i+1,op1-1,op2))
            if op2 and nums[i]>=k:
                ret = max(ret,k + dfs(i+1,op1,op2-1))
            if op1 and op2 :
                if nums[i]>=k*2-1:
                    ret = max(ret,nums[i]//2 + k + dfs(i+1,op1-1,op2-1))
                elif nums[i]>=k:
                    ret = max(ret,k + (nums[i] -k) //2 + dfs(i+1,op1-1,op2-1))
            
            return ret
        
        return sm - dfs(0,op1,op2)





        





re =Solution().minArraySum(nums = [882,307,624,469,329,684,851,608,317,205], k = 431, op1 =9, op2 = 4)
print(re)