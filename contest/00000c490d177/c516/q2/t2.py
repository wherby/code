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
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        dp = [0]*(upper+2)
        for a in nums:
            if lower<=a <=upper:
                dp[a] = 1 
        dp[upper+1] = 1
        ret = []
        pre=-1
        for i in range(lower,upper+2):
            if dp[i] ==1 and pre !=-1:
                ret.append([pre,i-1])
                pre= -1
            if dp[i] ==0 and pre ==-1:
                pre = i 
        return ret





re =Solution().findDisappearedNumbers( nums = [2,3,5], lower = 2, upper =3)
print(re)