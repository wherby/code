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
    def longestSubarray(self, nums: list[int], k: int) -> int:
        def getMX():
            dic = {}
            dic[0] = -1 
            acc =0
            mx = 0 
            
            for i,a in enumerate(nums):
                acc +=a 
                acc =acc%k 
                if acc in dic:
                    mx = max(mx,i-dic[acc])
                else:
                    dic[acc]= i
            return mx
        mx = getMX()
        n = len(nums)
        for i in range(n):
            nums[i] = -nums[i]
            mx= max(mx,getMX())
            nums[i] = - nums[i]
        return mx
            




re =Solution()
print(re)