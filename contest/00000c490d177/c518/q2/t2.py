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
    def countGoodRotations(self, nums: list[int]) -> int:
        n  = len(nums)
        nums = nums+nums
        pls = [0]
        for a in nums:
            pls.append(a +pls[-1])
        #print(pls) 
        m= n //2 
        cnt = 0
        for i in range(n):
            if pls[i+m] -pls[i] > pls[i+n]-pls[i+m]:
                cnt +=1
        return cnt





re =Solution().countGoodRotations( nums = [1,2,3,4,5,6])
print(re)