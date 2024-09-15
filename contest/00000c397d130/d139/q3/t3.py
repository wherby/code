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
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def getMax(ls):
            ret =[0]*128
            for i in range(127,-1,-1):
                acc= 0
                for a in ls:
                    if a&i == i:
                        acc +=1
                if acc >=k:
                    ret[i] =1
            return ret
        max= 0
        for i in range(k,n-k+1):
            ls1,ls2=nums[:i],nums[i:]
            ret1,ret2 = getMax(ls1),getMax(ls2)
            
        




re =Solution().maxValue(nums = [2,6,7], k = 1)
print(re)