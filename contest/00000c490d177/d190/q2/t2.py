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
    def maxValidSplits(self, nums: list[int]) -> int:
        def getMax(nums):
            n1 = len(nums)
            pre =[]
            pos =[]
            p1,p2 =0,0
            for i in range(n1):
                p1= math.gcd(p1,nums[i])
                p2 =math.gcd(p2,nums[-(1+i)])
                pre.append(p1)
                pos.append(p2)
            cnt =0
            for i in range(n1-1):
                if pre[i] == pos[-2-i]:
                    cnt +=1
            return cnt
        mx = getMax(nums)
        n = len(nums)
        for i in range(n):
            ls2 = nums[:i] + nums[i+1:]
            mx = max(mx,getMax(ls2))
        return mx




re =Solution().maxValidSplits([10,30,15,10])
print(re)