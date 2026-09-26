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
    def largestPower(self, nums: list[int]) -> list[int]:
        curMask = (1<<15)-1
        n =len(nums)
        perm =[]
        idx = 0
        nums.sort()
        while curMask !=0 and len(nums) :
            a = nums.pop()
            perm.append(a)
            if a != curMask:
                curMask = a & curMask
                nums = [a & curMask for a in nums]
                nums.sort()
                #print(perm,curMask)
        #print(perm)
        
        power = [0] * 15
        for i in range(15):
            bit_pos = 14 - i 
            count = 0
            for x in perm:
                if (x >> bit_pos) & 1:
                    count += 1
                else:
                    break  
            power[i] = count
        return power





re =Solution().largestPower([5,2,1,15,10])
print(re)