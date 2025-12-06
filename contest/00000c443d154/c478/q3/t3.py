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
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        ret =n=len(nums)
        dic = {}
        for i in range(n-1,-1,-1):
            t= int(str(nums[i])[::-1])
            if t in dic:
                ret = min(ret,dic[t]-i)
            dic[nums[i]] = i 
        return ret if ret != n else -1






re =Solution()
print(re)