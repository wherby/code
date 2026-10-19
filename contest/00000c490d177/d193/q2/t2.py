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
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        ret = 1
        l = 0
        for i,a in enumerate(nums):
            if a %k == nums[l] %k:
                if a %k ==0:
                    ret = max(ret, i-l+1)
                else:
                    d = a % k 
                    c = math.gcd(k,d)
                    l1 = k //c 
                    if l1 < i-l+1:
                        s1 = (i-l)// l1 *l1 +1 
                        ret = max(ret,s1) 
            else:
                l = i 
        return ret



re =Solution()
print(re)