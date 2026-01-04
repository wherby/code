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
    def minLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = n+1 
        dic = defaultdict(int)
        l =0 
        acc = 0 
        for i,a in enumerate(nums):
            if dic[a] == 0:
                acc +=a 
            dic[a] +=1 
            while acc >=k:
                ret = min(ret,i-l+1)
                
                dic[nums[l]] -=1 
                if dic[nums[l]] ==0:
                    acc -= nums[l]
                l +=1
        return ret if ret <=n else -1





re =Solution().minLength([9,20,25,20,28,20], k = 26)
print(re)