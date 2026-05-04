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
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        
        n = len(nums)
        toR = [0]
        for i in range(n):
            x1= 10**20
            if i>0:
                x1 = nums[i]-nums[i-1]
            x2 = 10**20
            if i < n-1:
                x2 = nums[i+1] -nums[i]
            if x1>x2:
                toR.append(toR[-1]+1)
            else:
                toR.append(toR[-1]+x2)
        toL = [0]
        for i in range(n-1,-1,-1):
            x1 = 10**20
            if i>0:
                x1 = nums[i]-nums[i-1]
            x2 = 10**20
            if i < n-1:
                x2 = nums[i+1] -nums[i]
            if x1<=x2:
                toL.append(toL[-1]+1)
            else:
                toL.append(toL[-1]+x1)
        re = []

        for a,b in queries:
            if a <b:
                re.append(toR[b]-toR[a])
            elif a>b:
                re.append(toL[n-b-1]-toL[n-a-1])
            else:
                re.append(0)
        return re





re =Solution().minCost(nums = [-5,-2,3], queries = [[0,2],[2,0],[1,2]])
print(re)