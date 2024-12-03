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

        for i,a in enumerate(nums):
            if a-a//2 >=k:
                if op1:
                    sm -=a//2
                    op1-=1
                    nums[i] -= a//2
                if op2:
                    sm -=k 
                    op2 -=1
                    nums[i] -= k
                nums[i] =0
            elif a ==k*2-1 and op1 and op2:
                op1 -=1
                op2 -=1
                sm -= a
                nums[i]=0
        #print(nums,sm,op1,op2)
        nums.sort()
        #print(nums)
        if k%2 ==0:
            for i,a in enumerate(nums):
                if a >=k and op2:
                    nums[i] -=k 
                    op2 -=1
                    sm -=k 
        else:
            for i,a in enumerate(nums):
                if a >=k and op2:
                    if a %2 ==1:
                        nums[i] -=k 
                        op2 -=1
                        sm -=k 
                    else:
                        
            
        nums.sort(reverse= True)
        print(nums,sm,op1,op2)
        for i,a in  enumerate(nums):
            if op1:
                sm -= a//2 
                op1 -=1
                nums[i] -=a//2
        print(nums,sm,op1,op2)
        return sm





        





re =Solution().minArraySum(nums = [882,307,624,469,329,684,851,608,317,205], k = 431, op1 =9, op2 = 4)
print(re)