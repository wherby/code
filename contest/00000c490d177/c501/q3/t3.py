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
    def minArraySum(self, nums: list[int]) -> int:
        mx = max(nums)+1
        ls = [0]*mx
        acc = 0
        for a in nums:
            ls[a]+=1
        for i in range(1,mx):
            if ls[i]:
                for j in range(i*2,mx,i):
                    if ls[j]:
                        ls[i] += ls[j]
                        ls[j] = 0 
                acc += i *ls[i]
        return acc
        

        





re =Solution().minArraySum(nums = [3,6,2])
print(re)