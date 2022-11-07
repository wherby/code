from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
#from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n  = len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i] *=2
                nums[i+1] = 0 
        ls = [0]*n
        idx = 0 
        #print(nums)
        for i in range(n):
            if nums[i] !=0:
                ls[idx] = nums[i]
                idx +=1
        for  i in range(n):
            nums[i] = ls[i]
        return nums





re =Solution().applyOperations([0,1])
print(re)