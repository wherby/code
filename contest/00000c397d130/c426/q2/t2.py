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
    def getLargestOutlier(self, nums: List[int]) -> int:
        sm = sum(nums)
        dic = defaultdict(int)
        for a in nums:
            dic[a] +=1
        ret = []
        for a in nums:
            sm = sm -a 
            dic[a] -=1
            if sm%2 ==0 and dic[sm//2] >0:
                ret.append(a)
            dic[a] +=1
            sm +=a 
        return max(ret)






re =Solution().getLargestOutlier([2,3,5,10])
print(re)