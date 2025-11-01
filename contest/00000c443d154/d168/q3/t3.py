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
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        lst = nums2[-1]
        mm = abs(lst-nums1[0] )
        cnt = 0
        for a,b in zip(nums1,nums2):
            cnt += abs(b-a)
            d =min(abs(a-lst),abs(b-lst))
            mm = min(mm,d)
            if (a-lst)*(lst-b)>0:
                mm = 0
            
        return cnt +mm+1





re =Solution().minOperations(nums1 = [2,8], nums2 = [1,7,3])
print(re)