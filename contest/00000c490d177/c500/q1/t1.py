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
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ls= [0,0]
        for a in nums:
            ls[a%2] +=1
        ret= []
        for i in range(n):
            t = (nums[i]+1)%2
            ret.append(ls[t])
            ls[(nums[i])%2] -=1
        return ret





re =Solution()
print(re)