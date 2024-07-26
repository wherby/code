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
    def minChanges(self, nums: List[int], k: int) -> int:
        c = defaultdict(list)
        n = len(nums)
        for i in range(n//2):
            c[abs(nums[i] - nums[n-1-i])].append(max(nums[i],nums[n-1-i],k-nums[i],k-nums[n-1-i]))
        ret = n
        sl = SortedList([])
        keys = sorted(list(c.keys()))
        for k in keys:
            t1 = sl.bisect_right(k-1)
            ret = min(ret,n//2 -len(c[k]) + t1)
            #print(k,c[k],t1,ret,sl)
            for a in c[k]:
                sl.add(a)
        return ret





# re =Solution().minChanges(nums = [1,0,1,2,4,3], k = 4)
# print(re)
re =Solution().minChanges(nums = [0,1,1,7,4,5,5,7,4,2,6,1,0,0,1,1,1,7,7,2], k = 7)
print(re,7)