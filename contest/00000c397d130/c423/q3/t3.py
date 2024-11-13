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
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        mod = 10**9+7
        
        dic =defaultdict(int)
        cdic= defaultdict(int)
        for a in nums:
            t = dic[a-1] + cdic[a-1]*a + dic[a+1] + cdic[a+1]*a +a
            cdic[a] += cdic[a-1] + cdic[a+1] + 1
            dic[a] +=t
        acc = 0
        for k,v in dic.items():
            acc +=v 
        return acc%mod





re =Solution().sumOfGoodSubsequences([3,4,5])
print(re)